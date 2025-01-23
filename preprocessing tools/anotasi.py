import os
import cv2
from ultralytics import YOLO

# Load your YOLOv8 model
model = YOLO('best.pt')  # Pastikan model 'best.pt' ada di direktori yang benar

# Define the directory containing the images and output directory
input_dir = 'Dataset-Athaya/test/melanoma'
output_dir = 'nyobain_anotasi'
os.makedirs(output_dir, exist_ok=True)

# Define the class label (in this case, dermatofibra)
class_label = 'melanoma'
class_id = 2  # Use 0 or another ID if you use YOLO format

# Loop through all images in the input directory
for img_file in os.listdir(input_dir):
    if img_file.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, img_file)
        img = cv2.imread(img_path)

        # Detect bounding boxes using the model
        results = model.predict(source=img, save=False)  # Disable save since you're manually saving labels

        # Check if any boxes are detected
        if len(results) > 0:
            boxes = results[0].boxes.xywh.cpu().numpy()  # Get bounding boxes (x_center, y_center, width, height)

            # Write annotations to a label file (YOLO format: class_id x_center y_center width height)
            label_file = os.path.join(output_dir, img_file.replace('.jpg', '.txt').replace('.png', '.txt'))
            with open(label_file, 'w') as f:
                for box in boxes:
                    x_center, y_center, width, height = box[:4]  # Only use the first 4 elements
                    f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

print(f"Annotations saved to {output_dir}")
