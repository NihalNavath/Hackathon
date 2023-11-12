from ultralytics import YOLO

def train_data():
    model = YOLO("yolov8n.yaml")

    model.train(data="config.yaml", epochs=1)

train_data()