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
