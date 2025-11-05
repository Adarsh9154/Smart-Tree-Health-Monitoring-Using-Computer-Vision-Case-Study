# 🌿 Smart Tree Health Monitoring using Computer Vision and Deep Learning

### 👨‍💻 Developed by: **Adarsh Mundhe**  
📘 Dept. of Data Science, SPPU

---

## 🧠 Overview
This project leverages **Computer Vision** and **Deep Learning (CNNs)** to automatically detect whether a **tree or plant leaf** is healthy or diseased.  
By analyzing visual features like **color, texture, and shape**, the system can classify diseases such as:

- 🍃 **Healthy**
- 🍂 **Bacterial Blight**
- 🍁 **Leaf Spot**
- 🌾 **Yellow Virus**

The main goal is to **assist farmers and environmental authorities** in monitoring plant health and ensuring **sustainable ecosystem management**.

---

## ⚙️ Tech Stack
| Technology | Purpose |
|-------------|----------|
| Python | Programming Language |
| TensorFlow / Keras | Model Building & Training |
| OpenCV | Image Preprocessing |
| Streamlit | Web App Interface |
| PlantVillage Dataset (Kaggle) | Training Dataset |

---

## 🚀 How It Works
1. **Data Collection:** Images are taken from the *PlantVillage* dataset.  
2. **Preprocessing:** All images are resized, normalized, and augmented.  
3. **Model Training:** A **CNN (MobileNetV2)** is trained to classify leaf diseases.  
4. **Prediction:** When a user uploads an image, the model predicts its health status.  
5. **Deployment:** The trained model is integrated into a **Streamlit web app** for easy interaction.

---

## 🧩 System Architecture
```
Leaf Image → Preprocessing → CNN Model → Classification → Result Visualization (Streamlit)
```

---

## 📊 Results
- ✅ **Accuracy:** 90–95%  
- ⚡ **Detection Time:** < 2 seconds per image  
- 🌱 **Impact:** Early detection helps prevent large-scale crop loss and supports sustainability.

---

## 🖥️ Installation & Usage
### 🔧 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/smart-tree-health-monitoring.git
cd smart-tree-health-monitoring
```

### 📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🧠 3. Train the Model
```bash
python train.py
```

### 🌐 4. Run the Web App
```bash
streamlit run app.py
```

---

## 🌍 Real-World Applications
- 🌳 **Smart Forest Monitoring** – Detect unhealthy trees automatically.  
- 🌾 **Agriculture** – Help farmers detect leaf diseases early.  
- 🏞️ **Urban Tree Management** – Monitor city trees for environmental protection.  
- 🧑‍🌾 **Farm Advisory Systems** – Provide data-driven health reports to farmers.

---

## 🔮 Future Scope
- Integrate **drone-based image collection** for large forest areas.  
- Combine with **IoT sensors** for real-time monitoring.  
- Extend model to **multiple crop species** and regional disease types.  
- Add **voice-assisted diagnosis** for farmers.

---

## 🏆 Key Features
- Automated leaf disease classification  
- Real-time prediction dashboard  
- High accuracy using CNN architecture  
- Lightweight model suitable for deployment  

---

## 📸 Demo
You can try the demo version here (no training needed):  
👉 **[Demo App (Streamlit-ready)]([https://share.streamlit.io](https://smart-tree-health-monitoring-using-computer-vision-case-study.streamlit.app/))** *(Upload your leaf image and see prediction results)*

---

## 🧾 Dataset Reference
- **PlantVillage Dataset:** [Kaggle Link](https://www.kaggle.com/emmarex/plantdisease)

---

## 🏷️ Keywords
`Computer Vision` • `Deep Learning` • `CNN` • `Smart Agriculture` • `AI for Environment` • `Plant Disease Detection`

---

## 📬 Contact
📧 **Adarsh Mundhe**  
Dept. of Data Science, SPPU  
💼 [LinkedIn Profile](https://www.linkedin.com/in/adarsh-mundhe-07247827b/)  
🌟 Star this repo if you like it!

---

> “AI can help nature heal itself — one leaf at a time.” 🌿
