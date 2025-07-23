# beebot-marigold-detector
A YOLOv5-based flower detection model trained to identify marigold flowers for the AI Pollination Bot (BeeBot).

## 📦 Features
- Downloads dataset from Roboflow
- Trains YOLOv5 model on marigold dataset
- Skips uploading large datasets to GitHub

## 🚀 Quickstart
1. Clone the repo
2. Add your Roboflow API key in `download_data.py`
3. Run:
    ```bash
    python download_data.py
    python train.py
    ```
4. Your model will be saved in the `runs/train/` folder.

## 🛠 Requirements
- Python 3.8+
- torch, torchvision
- Roboflow SDK
- [YOLOv5](https://github.com/ultralytics/yolov5)

## 🧐 Output
A custom-trained model ready to deploy on BeeBot via TFLite or Raspberry Pi.
"""

