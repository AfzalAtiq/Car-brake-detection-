from ultralytics import YOLO

# Load a COCO-pretrained YOLO11s-cls model
model = YOLO("D:/Afzal/ltIntern/Image PT/yolo11n-cls.pt")

# Train the model
results = model.train(data="Datasets", epochs=10, imgsz=640)
