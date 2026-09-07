from ultralytics import YOLO

model = YOLO("yolo26s.pt")

model.train(
    data="/home/lab114/tank-detection-model/dataset/yolocodemuti-view-tank-dataset-yolo26.ndjson",
    epochs=100,
    imgsz=512,
    batch=48,
    device=0,
    workers=0,
    project="/home/lab114/tank-detection-model/runs",
    name="yolo26s_512"
)


