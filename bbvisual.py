import cv2

def visualize_bounding_boxes(image_path, bounding_boxes_path):
    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to a smaller size for visualization
    scale_percent = 70  # Adjust the scale as needed
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    image = cv2.resize(image, (width, height))
    
    # Read the bounding box coordinates from the text file
    with open(bounding_boxes_path, 'r') as f:
        lines = f.readlines()
    
    # Draw bounding boxes on the resized image
    for line in lines:
        line = line.strip().split()
        class_id = int(line[0])
        x = int(float(line[1]) * width)
        y = int(float(line[2]) * height)
        w = int(float(line[3]) * width)
        h = int(float(line[4]) * height)
        
        # Draw the bounding box rectangle
        color = (0, 255, 0)  # Green color
        thickness = 2
        x = int (x-(w/2))
        y = int (y-(h/2))
        print(class_id,x,y,w,h)
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness)
        
        # Add the class label
        label = f'Class {class_id}'
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        cv2.putText(image, label, (x, y-10), font, font_scale, color, thickness)
    
    # Display the resized image with bounding boxes
    cv2.imshow('Bounding Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the paths to your image and bounding boxes file
image_path = r"C:\Users\aless\Documents\GitHub\stm32ai\zoo\stm32ai-modelzoo\BBvisualI\amz_00071.jpg"
bounding_boxes_path = r"C:\Users\aless\Documents\GitHub\stm32ai\zoo\stm32ai-modelzoo\BBvisualA\amz_00071.txt"

# Call the function to visualize the bounding boxes
visualize_bounding_boxes(image_path, bounding_boxes_path)
