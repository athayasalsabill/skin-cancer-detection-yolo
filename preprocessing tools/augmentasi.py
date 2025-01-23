import os
import random
import cv2
import albumentations as A
import shutil

# Fungsi untuk augmentasi gambar
def augment_image(image):
    # Definisikan transformasi augmentasi
    transform = A.Compose([
        A.OneOf([
            A.HorizontalFlip(p=0.5),
            A.VerticalFlip(p=0.5),
        ], p=1),
        A.OneOf([
            A.Rotate(limit=90, p=0.5),
            A.Rotate(limit=(-90), p=0.5),
        ], p=1),
        A.Rotate(limit=15, p=0.5),
        A.ColorJitter(brightness=0.25, contrast=0, saturation=0.25, hue=0, p=0.5),
    ])
    
    # Terapkan augmentasi
    augmented = transform(image=image)
    return augmented['image']

# Fungsi untuk melakukan augmentasi hingga mencapai target jumlah gambar
def augment_dataset(train_folder, target_count=4750):
    # Dapatkan daftar kelas (subfolder)
    classes = [d for d in os.listdir(train_folder) if os.path.isdir(os.path.join(train_folder, d))]

    for class_name in classes:
        class_path = os.path.join(train_folder, class_name)
        images = [img for img in os.listdir(class_path) if img.endswith(('.jpg', '.jpeg', '.png'))]
        original_images = images.copy()
        
        # Hitung jumlah gambar yang perlu di-augmentasi
        if len(images) >= target_count:
            print(f"Class {class_name} already has {len(images)} or more images. No augmentation needed.")
            continue
        
        augment_needed = target_count - len(images)
        print(f"Class {class_name} - Augmenting {augment_needed} images.")
        
        # Augment gambar hingga mencapai jumlah yang ditargetkan
        while len(images) < target_count:
            # Pilih gambar secara acak untuk di-augmentasi
            img_name = random.choice(original_images)
            img_path = os.path.join(class_path, img_name)
            img = cv2.imread(img_path)
            
            if img is None:
                print(f"Failed to load image {img_name}. Skipping.")
                continue
            
            # Augmentasi gambar
            augmented_img = augment_image(image=img)
            
            # Simpan gambar hasil augmentasi
            new_img_name = f"aug_{len(images)+1}_{img_name}"
            new_img_path = os.path.join(class_path, new_img_name)
            cv2.imwrite(new_img_path, augmented_img)
            
            images.append(new_img_name)

# Path ke folder train
train_folder = 'Dataset-Athaya-4.0-resize/train'

# Augment dataset hingga setiap kelas memiliki 4750 gambar
augment_dataset(train_folder, target_count=3500)
