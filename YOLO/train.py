from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()

# Import a pretrained model 
    model = YOLO(r'C:\Users\aless\Desktop\yolov8\yolo\Lib\site-packages\ultralytics\cfg\models\v8\yolov8.yaml').load(r'C:\Users\aless\Desktop\yolov8\yolov8n.pt')  # build from YAML and transfer weights
    #il file yaml contiene la topologia del modello (installato automaticamente con ultralytics).
    #il file yolov8.pt contiene il modello preallenato (installato automaticamente con ultralytics).

# Train the model 
    results = model.train(data= r'C:/Users/aless\Desktop/yolov8/data.yaml', epochs=100, batch = -1, imgsz = 1024, cos_lr = True, workers = 32)

# Per visualizzare i risultati in tensorboard utilizzo il seguente comando
# tensorboard --logdir ultralytics/runs  # replace with 'runs' directory