from ultralytics import YOLO

# model = YOLO("yolov8n.pt")
# model = YOLO("yolov8s.pt")
# model = YOLO("yolov8m.pt")
model = YOLO("yolov8l.pt")

results = model(source="tokyo-2.jpg", show=True, conf=0.2, save=True) # L - 480x640 26 persons, 1 bicycle, 3 cars, 4 backpacks, 15 handbags, 574.5ms; n - 480x640 15 persons, 2 cars, 1 suitcase, 65.7ms
# results = model(source="tokyo.jpg", show=True, conf=0.4, save=True) # L - 480x640 12 persons, 5 cars, 2 trucks, 3 handbags, 611.8ms; n - 480x640 9 persons, 4 cars, 2 trucks, 84.7ms
# results = model(source=0, show=True, conf=0.4, save=True)
