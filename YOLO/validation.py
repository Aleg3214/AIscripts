from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()
    
# load a custom model (best model)
    model = YOLO(r"C:\Users\aless\Desktop\best\best.pt")

    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map    # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps   # a list contains map50-95 of each category