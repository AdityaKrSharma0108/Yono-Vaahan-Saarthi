import traceback
try:
    from ultralytics import YOLO
    print("Ultralytics imported successfully.")
    model = YOLO("new.onnx", task='detect')
    print("YOLO model initialized successfully.")
except Exception as e:
    print("Exception occurred:")
    traceback.print_exc()
