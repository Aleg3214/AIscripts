from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()

# load a custom trained model (best model)
    model = YOLO(r'C:\Users\aless\Desktop\yolov8\runs\detect\train4\weights\best.pt')

# Export the model
    model.export(format='tflite', imgsz = 256, int8 = True, half = True)
