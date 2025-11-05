
import streamlit as st
import numpy as np
from PIL import Image, ImageFilter
from io import BytesIO

st.set_page_config(page_title="Smart Tree Health Demo", page_icon="🌿", layout="centered")
st.title("🌿 Smart Tree Health Monitoring — Demo (No Trained Model Needed)")
st.write("Upload a leaf image to see a **demo prediction** using simple color/texture heuristics.")

CLASSES = ["Healthy", "Bacterial_Blight", "Leaf_Spot", "Yellow_Virus"]

def simple_features(img):
    # Resize for speed
    img = img.resize((256, 256)).convert("RGB")
    arr = np.array(img) / 255.0

    # Color stats
    mean_rgb = arr.mean(axis=(0,1))  # R, G, B means
    std_rgb = arr.std(axis=(0,1))

    # Greeness score (G - (R+B)/2)
    greenness = mean_rgb[1] - 0.5*(mean_rgb[0] + mean_rgb[2])

    # Yellow-ish detection (high R and G, low B)
    yellow_score = (mean_rgb[0] + mean_rgb[1]) / 2 - mean_rgb[2]

    # Spot score via high frequency energy
    gray = (0.299*arr[:,:,0] + 0.587*arr[:,:,1] + 0.114*arr[:,:,2])
    # Sobel-like simple gradient magnitude
    gx = np.abs(np.diff(gray, axis=1)).mean()
    gy = np.abs(np.diff(gray, axis=0)).mean()
    edge_energy = (gx + gy) / 2

    return dict(
        mean_r=float(mean_rgb[0]), mean_g=float(mean_rgb[1]), mean_b=float(mean_rgb[2]),
        std_r=float(std_rgb[0]), std_g=float(std_rgb[1]), std_b=float(std_rgb[2]),
        greenness=float(greenness), yellow_score=float(yellow_score), edge_energy=float(edge_energy)
    )

def heuristic_predict(feat):
    # Start with healthy
    scores = {c: 0.0 for c in CLASSES}
    # Healthy if strong greenness and low edges (smooth leaf) and low yellow
    scores["Healthy"] = 0.6*feat["greenness"] - 0.3*feat["yellow_score"] - 0.2*feat["edge_energy"]

    # Leaf Spot -> high edge energy (speckles/contrast)
    scores["Leaf_Spot"] = 0.8*feat["edge_energy"] + 0.1*(feat["std_r"]+feat["std_g"]+feat["std_b"])

    # Yellow Virus -> high yellow_score, low greenness
    scores["Yellow_Virus"] = 1.0*feat["yellow_score"] - 0.5*feat["greenness"]

    # Bacterial Blight -> not very yellow, medium edges, lower greenness
    scores["Bacterial_Blight"] = 0.5*feat["edge_energy"] + 0.2*(1 - feat["greenness"]) - 0.1*feat["yellow_score"]

    # Convert to softmax-like probabilities
    xs = np.array(list(scores.values()), dtype=np.float32)
    xs = (xs - xs.mean()) / (xs.std() + 1e-6)
    exps = np.exp(xs)
    probs = exps / exps.sum()

    return dict(zip(CLASSES, probs.tolist())), scores

st.sidebar.header("About this demo")
st.sidebar.info(
    "This is a **demo-only** heuristic model for classroom presentation. "
    "It estimates classes using simple color/texture features — no training required.\n\n"
    "For a real model, use the training code I provided (MobileNetV2 transfer learning)."
)

uploaded = st.file_uploader("Upload a leaf image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    feat = simple_features(img)
    probs, raw = heuristic_predict(feat)

    # Display prediction
    pred_cls = max(probs, key=probs.get)
    st.subheader(f"Prediction: **{pred_cls}**")
    st.write(f"Confidence: **{probs[pred_cls]*100:.1f}%** (demo heuristic)")

    st.markdown("**Class probabilities (demo):**")
    for k,v in probs.items():
        st.write(f"- {k}: {v*100:.1f}%")

    st.markdown("**Quick care tips:**")
    tips = {
        "Healthy": "Looks fine. Maintain balanced watering and sunlight.",
        "Bacterial_Blight": "Prune infected areas. Consider copper-based bactericide.",
        "Leaf_Spot": "Improve airflow; avoid overhead watering; fungicide if needed.",
        "Yellow_Virus": "Isolate plant; control aphids/whiteflies; consult an agronomist."
    }
    st.info(tips.get(pred_cls, "Consult a plant pathologist for precise treatment."))

    with st.expander("Show extracted features (for explanation)"):
        st.json(feat)
else:
    st.caption("Tip: Clear, close-up leaf photos work best for this demo.")
