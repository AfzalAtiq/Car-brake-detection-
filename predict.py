from ultralytics import YOLO
model = YOLO("D:/Afzal/ltIntern/Image PT/runs/classify/train3/weights/best.pt")

results = model("D:/Afzal/ltIntern/Image PT/tests_images/image5.jpg")  #save=True, imgsz=320, conf=0.5)
results[0].show()