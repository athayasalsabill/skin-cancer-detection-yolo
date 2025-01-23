import os
import cv2
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan gambar dengan bounding box
def draw_bounding_boxes(image_path, label_path, class_names=None):
    # Load image
    img = cv2.imread(image_path)
    h, w, _ = img.shape  # Get image height and width

    # Load YOLO format label file
    with open(label_path, 'r') as f:
        labels = f.readlines()

    # Loop over each line in the label file
    for label in labels:
        label_data = label.strip().split()
        class_id = int(label_data[0])  # YOLO format class id
        x_center, y_center, bbox_width, bbox_height = map(float, label_data[1:])

        # Convert normalized YOLO format (x_center, y_center, width, height) to pixel values
        x_center = int(x_center * w)
        y_center = int(y_center * h)
        bbox_width = int(bbox_width * w)
        bbox_height = int(bbox_height * h)

        # Calculate top-left corner and bottom-right corner of bounding box
        x1 = int(x_center - bbox_width / 2)
        y1 = int(y_center - bbox_height / 2)
        x2 = int(x_center + bbox_width / 2)
        y2 = int(y_center + bbox_height / 2)

        # Draw bounding box on image
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 15)

        # Optionally put class name on bounding box
        if class_names and class_id < len(class_names):
            label_text = class_names[class_id]
            cv2.putText(img, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 5, (36, 255, 120), 15)

    # Convert BGR (OpenCV format) to RGB for display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display image with bounding boxes using matplotlib
    plt.figure(figsize=(8, 8))
    plt.imshow(img_rgb)
    plt.axis('off')  # Hide axes
    plt.show()

# Path ke gambar dan file label .txt
image_path = 'Dataset-Athaya/test/melanoma/ISIC_0068744.txt'
label_path = 'nyobain_anotasi/ISIC_0068744.txt'

# Daftar nama kelas (opsional)
class_names = ['vascular lesion', 
               'squamous cell carcinoma', 
               'melanoma',
              'actinic keratosis']  # Ganti dengan nama kelas sebenarnya

# Panggil fungsi untuk menampilkan gambar dengan bounding box
draw_bounding_boxes(image_path, label_path, class_names=class_names)
