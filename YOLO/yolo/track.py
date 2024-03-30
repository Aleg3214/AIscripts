from ultralytics import YOLO
import torch
import multiprocessing
from multiprocessing import spawn
from multiprocessing.spawn import *

if __name__ == '__main__':
    freeze_support()
# Load a custom trained model (best model)
    model = YOLO(r'C:\Users\aless\Desktop\yolov8\runs\detect\train16\weights\best.pt')

# Perform tracking with the model
    #results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True)  # Tracking with default tracker
    results = model.track(source="https://www.youtube.com/watch?v=4Jkji_BEUqY", show=True, tracker="bytetrack.yaml", conf = 0.3, iou = 0.5, imgsz = 256)  # Tracking with ByteTrack tracker



# Yolov8 code for custom tracking

'''
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
video_path = "path/to/your/video/file.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
'''
