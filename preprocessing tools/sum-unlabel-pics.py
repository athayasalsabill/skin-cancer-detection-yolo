import os

# Fungsi untuk menghitung dan menampilkan gambar yang tidak mempunyai file label .txt
def find_images_without_labels(image_dir, label_dir):
    missing_labels = []
    
    # Loop melalui semua gambar di folder image_dir
    for img_file in os.listdir(image_dir):
        if img_file.endswith(('.jpg', '.jpeg', '.png')):
            # Nama file label yang sesuai dengan file gambar
            label_file = os.path.join(label_dir, img_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))
            
            # Jika file label tidak ada, tambahkan ke daftar missing_labels
            if not os.path.exists(label_file):
                missing_labels.append(img_file)
    
    # Tampilkan hasil
    print(f"Total images without labels: {len(missing_labels)}")
    if missing_labels:
        print("List of images without labels:")
        for img in missing_labels:
            print(img)
    else:
        print("All images have labels.")

    return missing_labels

# Path ke folder Dataset
dataset_base_dir = 'Dataset-Athaya'


# Cek di folder 'train' dan 'valid'
train_image_dir = os.path.join(dataset_base_dir, 'train')
train_label_dir = os.path.join(dataset_base_dir, 'labels')

valid_image_dir = os.path.join(dataset_base_dir, 'valid')
valid_label_dir = os.path.join(dataset_base_dir, 'labels-valid')

# Cek gambar tanpa label di folder train
print("Checking missing labels in train dataset:")
train_missing_labels = []
for class_name in os.listdir(train_image_dir):
    class_image_dir = os.path.join(train_image_dir, class_name)
    class_label_dir = os.path.join(train_label_dir, class_name)
    train_missing_labels.extend(find_images_without_labels(class_image_dir, class_label_dir))

# Cek gambar tanpa label di folder valid
print("\nChecking missing labels in valid dataset:")
valid_missing_labels = []
for class_name in os.listdir(valid_image_dir):
    class_image_dir = os.path.join(valid_image_dir, class_name)
    class_label_dir = os.path.join(valid_label_dir, class_name)
    valid_missing_labels.extend(find_images_without_labels(class_image_dir, class_label_dir))

# Total gambar tanpa label di kedua folder
print("\nSummary:")
total_missing_labels = len(train_missing_labels) + len(valid_missing_labels)
print(f"Total images without labels in train: {len(train_missing_labels)}")
print(f"Total images without labels in valid: {len(valid_missing_labels)}")
print(f"Total images without labels in both train and valid: {total_missing_labels}")
