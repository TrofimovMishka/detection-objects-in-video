from ultralytics import YOLO

# model = YOLO("yolov8n.pt")
# model = YOLO("yolov8s.pt")
# model = YOLO("yolov8m.pt")
model = YOLO("yolov8l.pt")

results = model(source="tokyo-2.jpg", show=True, conf=0.2, save=True)
# results = model(source="tokyo.jpg", show=True, conf=0.4, save=True)
# results = model(source=0, show=True, conf=0.4, save=True)

# import cv2
#
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Error opening camera (index 0)")
#     cap = cv2.VideoCapture(1)
#     if not cap.isOpened():
#         print("Error opening camera (index 1)")
# else:
#     print("Cap is opened")
#     cap.release()