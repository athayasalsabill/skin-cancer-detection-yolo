import os
import random

# Path ke folder "basal cell carcinoma"
folder_path = 'Dataset/basal-cell-carcinoma'

# Daftar file gambar yang ada di dalam folder
image_files = [img for img in os.listdir(folder_path) if img.endswith(('.jpg', '.jpeg', '.png'))]

# Cek apakah ada cukup gambar untuk dihapus
if len(image_files) >= 84:
    # Pilih 84 gambar secara acak
    images_to_delete = random.sample(image_files, 84)
    
    # Hapus gambar yang dipilih
    for img in images_to_delete:
        img_path = os.path.join(folder_path, img)
        os.remove(img_path)
        print(f"Deleted {img}")
else:
    print("Tidak ada cukup gambar untuk dihapus, hanya ada", len(image_files), "gambar dalam folder.")

