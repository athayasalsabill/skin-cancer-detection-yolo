import os

# Fungsi untuk menghapus gambar yang tidak memiliki file label .txt
def delete_images_without_labels(image_dir, label_dir):
    deleted_images = []

    # Loop melalui semua gambar di folder image_dir
    for img_file in os.listdir(image_dir):
        if img_file.endswith(('.jpg', '.jpeg', '.png')):
            # Nama file label yang sesuai dengan file gambar
            label_file = os.path.join(label_dir, img_file.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt'))

            # Jika file label tidak ada, hapus gambar
            if not os.path.exists(label_file):
                img_path = os.path.join(image_dir, img_file)
                os.remove(img_path)  # Menghapus gambar
                deleted_images.append(img_file)  # Tambahkan gambar yang dihapus ke daftar

    # Tampilkan hasil
    print(f"Total images deleted: {len(deleted_images)}")
    if deleted_images:
        print("List of deleted images:")
        for img in deleted_images:
            print(img)
    else:
        print("No images were deleted. All images have labels.")

# Path ke folder Dataset
dataset_base_dir = 'Dataset-Athaya'

# Cek di folder 'train' dan 'valid'
train_image_dir = os.path.join(dataset_base_dir, 'train')
train_label_dir = os.path.join(dataset_base_dir, 'labels')

valid_image_dir = os.path.join(dataset_base_dir, 'valid')
valid_label_dir = os.path.join(dataset_base_dir, 'labels-valid')

# Hapus gambar tanpa label di folder train
print("Deleting images without labels in train dataset:")
for class_name in os.listdir(train_image_dir):
    class_image_dir = os.path.join(train_image_dir, class_name)
    class_label_dir = os.path.join(train_label_dir, class_name)
    delete_images_without_labels(class_image_dir, class_label_dir)

# Hapus gambar tanpa label di folder valid
print("\nDeleting images without labels in valid dataset:")
for class_name in os.listdir(valid_image_dir):
    class_image_dir = os.path.join(valid_image_dir, class_name)
    class_label_dir = os.path.join(valid_label_dir, class_name)
    delete_images_without_labels(class_image_dir, class_label_dir)
