from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()

# load a partially trained model (last model)
    model = YOLO(r'C:\Users\aless\Desktop\yolov8\runs\detect\train25\weights\last.pt')

# Resume training
    model.train(resume=True) #Posso resumare un training cambiando anche il numero di epoche o il dataset