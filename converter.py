import json
import glob
import os

def convert_to_yolo(json_data, image_width, image_height):
    objects = json_data["objects"]
    yolo_lines = []
    
    for obj in objects:
        global label
        if(obj["classTitle"] == "blue_cone"):
            label = 0
        elif (obj["classTitle"] == "yellow_cone"):
            label = 1
        elif (obj["classTitle"] == "orange_cone"):
            label = 2
        elif (obj["classTitle"] == "large_orange_cone"):
            label = 3
        class_title = label
        #class_title = obj["classTitle"]
        x_min, y_min = obj["points"]["exterior"][0]
        x_max, y_max = obj["points"]["exterior"][1]
        
        # Convert coordinates to YOLO format
        x_center = (x_min + x_max) / (2 * image_width)
        y_center = (y_min + y_max) / (2 * image_height)
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height
        
        # Append the YOLO line to the list
        yolo_line = f"{class_title} {x_center} {y_center} {width} {height}"
        yolo_lines.append(yolo_line)
    
    return yolo_lines

def process_files(input_dir, output_dir):
    # Get the list of JSON files in the input directory
    json_files = glob.glob(os.path.join(input_dir, "*.json"))

    for json_file in json_files:
        # Read the JSON file
        with open(json_file) as f:
            json_data = json.load(f)

        # Extract image width and height
        image_width = json_data["size"]["width"]
        image_height = json_data["size"]["height"]

        # Convert to YOLO format
        yolo_lines = convert_to_yolo(json_data, image_width, image_height)

        # Save the YOLO lines to a text file
        output_file = os.path.splitext(os.path.basename(json_file))[0] + ".txt"
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, "w") as f:
            f.write("\n".join(yolo_lines))

# Example usage
input_directory = ""   #file con annotazioni da convertire
output_directory = ""   #file dove mettere annotazione convertite

process_files(input_directory, output_directory)