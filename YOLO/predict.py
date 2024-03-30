from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()


# load a partially trained model (best model)
    model = YOLO(r'C:\Users\aless\Desktop\yolov8\runs\detect\T-1°model\weights\best.pt')

# Define path to directory containing images and videos for inference
    #source = r'C:\Users\aless\Desktop\yolov8\yolo\test2\images'
    source="https://www.youtube.com/watch?v=4Jkji_BEUqY"

# Run batched inference on a list of images
    results = model(source, show = True, stream=True, imgsz = 256, conf = 0.1, iou = 0.1, save = False, save_conf = False, max_det = 100)  # return a generator of Results objects

#Use stream=True for processing long videos or large datasets to efficiently manage memory.
#When stream=False, the results for all frames or data points are stored in memory,
#which can quickly add up and cause out-of-memory errors for large inputs. 
#In contrast, stream=True utilizes a generator, which only keeps the results of the current 
#frame or data point in memory, significantly reducing memory consumption and preventing out-of-memory issues

# Process results generator
    for result in results:
        result.plot(conf = True, labels = True, Boxes = True, probs = True)



