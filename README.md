├── Datasets/
│   ├── train/
│   │   ├── brake_on/
│   │   └── brake_off/
│   ├── val/
│   │   ├── brake_on/
│   │   └── brake_off/
├── yolo11n-cls.pt             # Pretrained YOLOv8 classification model
├── data.yaml                  # Dataset configuration
├── train_model.py             # Model training script
├── predict_brake.py           # Script for making predictions
├── main.py                    # Optional main file
├── predict.py                 # Optional earlier prediction file
```

---

## ✅ Features

- Binary classification: `brake_on` or `brake_off`
- Based on YOLOv8 classification
- Custom dataset support
- Training and prediction scripts included
- High accuracy with real-time results

---

## 📦 Installation

```bash
git clone https://github.com/AfzalAtiq/Car-brake-detection-/tree/master
cd brake-light-detection
pip install ultralytics
## 🚀 Training

```bash
python train_model.py
```

---

## 🔍 Prediction

```bash
python predict_brake.py
```
