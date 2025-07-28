# Jetbot-Collision-Avoidance
Real-Time Obstacle Avoidance on JetBot using AlexNet
# 🤖 JetBot Collision Avoidance using Deep Learning (AlexNet)

This project implements **real-time obstacle avoidance** on the [JetBot](https://github.com/NVIDIA-AI-IOT/jetbot) platform using a **camera feed and deep learning classification model**. The robot detects whether the path is **blocked or free**, and navigates accordingly.

![Demo](media/result_demo.gif)

---

## 🚀 Project Goal

To make a small NVIDIA JetBot **autonomously avoid obstacles** by analyzing the camera feed in real time using a lightweight convolutional neural network (AlexNet or ResNet18).

---

## 🎯 Key Features

- 🔍 **Real-time camera processing** via GStreamer + OpenCV
- 🧠 **Deep learning inference** using PyTorch + GPU (fp16)
- 🧭 **Autonomous navigation** with simple logic
- ⚙️ Runs directly on Jetson Nano without cloud dependency
- 🛠️ Handles **camera initialization**, model loading, and motor control

---

## 📦 Hardware and Software Used

| Component              | Details                         |
|------------------------|----------------------------------|
| Robot Base             | Yahboom JetBot Kit              |
| Camera                 | Jetson CSI camera               |
| Controller Board       | Jetson Nano (4GB)               |
| OS                     | JetBot SD Image (JP4.6)         |
| Framework              | PyTorch, torchvision            |
| Inference Optimization | FP16 / Half precision           |
| Camera Interface       | GStreamer (nvarguscamerasrc)    |
| Display                | Widgets (for Jupyter preview)   |

---

## 🧠 Model Details

The model is trained to classify camera images into two categories:
- **Blocked** – if there’s an obstacle ahead
- **Free** – if the path is clear

Models used:
- `AlexNet` (Modified final FC layer to output 2 classes)
- Optionally `ResNet18` for better accuracy

---

## 📁 Project Structure

