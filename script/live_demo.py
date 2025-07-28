import torch
import torchvision
import cv2
import numpy as np
import time
from jetbot import Camera, Robot, bgr8_to_jpeg
import torchvision.transforms as transforms
import torch.nn.functional as F

# Load model
model = torchvision.models.alexnet(pretrained=False)
model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, 2)
model.load_state_dict(torch.load('best_model.pth'))
device = torch.device('cuda')
model = model.to(device).eval().half()

# Preprocessing
mean = 255.0 * np.array([0.485, 0.456, 0.406])
stdev = 255.0 * np.array([0.229, 0.224, 0.225])
normalize = transforms.Normalize(mean, stdev)

def preprocess(image):
    x = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    x = x.transpose((2, 0, 1))
    x = torch.from_numpy(x).float()
    x = normalize(x)
    x = x.to(device).half()
    x = x[None, ...]
    return x

# Initialize camera and robot
camera = Camera.instance(width=224, height=224)
robot = Robot()

# Run loop
try:
    while True:
        frame = camera.value
        x = preprocess(frame)
        y = model(x)
        y = F.softmax(y, dim=1)
        prob_blocked = float(y.flatten()[0])
        print("Blocked probability:", prob_blocked)

        if prob_blocked < 0.5:
            robot.forward(0.7)
        else:
            robot.left(0.7)

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping robot...")
    robot.stop()
    camera.stop()
