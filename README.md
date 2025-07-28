# 🤖 JetBot Collision Avoidance using Deep Learning (AlexNet)

This project implements **real-time obstacle avoidance** on the [JetBot](https://github.com/NVIDIA-AI-IOT/jetbot) platform using a **camera feed and deep learning classification model**. The robot detects whether the path is **blocked or free**, and navigates accordingly. Click [here](https://youtu.be/xOFaC9Rw5iY) to check the final outcome

---

##  Project Goal

To make a small NVIDIA JetBot **autonomously avoid obstacles** by analyzing the camera feed in real time using a lightweight convolutional neural network (AlexNet or ResNet18).

---

##  Features Involved

- 🔍 **Real-time camera processing** via GStreamer + OpenCV
- 🧠 **Deep learning inference** using PyTorch + GPU (fp16)
- 🧭 **Autonomous navigation** with simple logic
- ⚙️ Runs directly on Jetson Nano without cloud dependency
- 🛠️ Handles **camera initialization**, model loading, and motor control

---

##  Hardware and Software Used

| Component              | Details                         |
|------------------------|----------------------------------|
| Robot Base             | Yahboom JetBot Kit              |
| Camera                 | Jetson CSI camera               |
| Controller Board       | Jetson Nano (4GB)               |
| OS                     | JetBot SD Image (JP4.6)         |
| Framework              | PyTorch, torchvision            |
| Inference Optimization | FP16 / Half precision           |
| Camera Interface       | GStreamer (nvarguscamerasrc)    |


---

##  Model Details

The model is trained to classify camera images into two categories:
- **Blocked** – if there’s an obstacle ahead
- **Free** – if the path is clear


---

## 📸 Data Collection

To train the collision avoidance model, we manually collected data using the JetBot's camera in various indoor environments. The data consists of labeled image frames representing two classes:

* **Blocked (label `0`)** – when an obstacle (e.g., wall, chair, or person) is directly in front of the robot.
* **Free (label `1`)** – when the path ahead is clear and the robot can safely move forward.

### How the Data Was Collected:

* **Environment**: Living room floor, narrow hallways, desk areas.
* **Lighting Conditions**: Varied — natural daylight, indoor lights, and low-light situations.
* **Recording Tool**: A custom Jupyter notebook using the JetBot camera feed, saving images with timestamps and labels.
* **Labeling Method**: While monitoring the live camera feed, we manually pressed buttons to classify each frame as “blocked” or “free”. Each image was saved with a label into separate folders:
    * `dataset/blocked/`
    * `dataset/free/`

### Dataset Summary:

| Class     | Samples    |
| --------- | ---------- |
| Blocked   | \~140      |
| Free      | \~140      |
| **Total** | **\~280** |

> 🔍 Note: Balanced dataset is crucial to prevent model bias toward any class.

### Preprocessing:

* Images were resized to **224×224** (matching input of AlexNet).
* Normalized using ImageNet stats:

  * Mean: `[0.485, 0.456, 0.406]`
  * Std: `[0.229, 0.224, 0.225]`

The dataset was later split into **training (80%)** and **validation (20%)** sets for model training.
📁 You can download some samples of the dataset from the [sample_data/dataset.zip](./sample_data/dataset.zip) folder in this repository.

---
  

Models used:
- `AlexNet` (Modified final FC layer to output 2 classes)
---

📚 For additional guidance, setup details, or troubleshooting, please refer to the official [NVIDIA JetBot GitHub repository](https://github.com/NVIDIA-AI-IOT/jetbot). And for example notebooks for data collection, training and executing the model please refer to [NVIDIA's official collision_avoidance folder](https://github.com/NVIDIA-AI-IOT/jetbot/tree/master/notebooks/collision_avoidance)




