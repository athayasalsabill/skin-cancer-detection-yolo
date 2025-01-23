""""ini buat hitung gambar untuk struktur dataset seperti berikut
/Dataset 
├── train 
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
├── valid 
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
├── test
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
"""
import os

def count_images_in_folders(root_folder):
  """Counts images in subfolders of a given root folder.

  Args:
    root_folder: The path to the root folder.

  Returns:
    A dictionary where keys are folder names and values are the number of image
    files (with extensions .jpg, .jpeg, .png) in each folder.
  """
  image_counts = {}
  for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
      count = 0
      for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
          count += 1
      image_counts[folder_name] = count
  return image_counts


train_counts = count_images_in_folders('C:/file D/Teknik Elektro/Riset Skin Cancer Claassification/dataset dari open source/SkinLesionDetection.v2i.yolov8/train')
valid_counts = count_images_in_folders('C:/file D/Teknik Elektro/Riset Skin Cancer Claassification/dataset dari open source/SkinLesionDetection.v2i.yolov8/valid')

#test_counts = count_images_in_folders('Dataset-Athaya-3.0/test')

print("Train Folder Image Counts:")
for folder, count in train_counts.items():
  print(f"{folder}: {count} images")

print("\nValid Folder Image Counts:")
for folder, count in valid_counts.items():
  print(f"{folder}: {count} images")

"""print("\nTest Folder Image Counts:")
for folder, count in test_counts.items():
  print(f"{folder}: {count} images")"""
