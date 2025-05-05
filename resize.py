from PIL import Image
import os

# Folder foto asli kamu
input_folder = 'fotopenyengat'  # <- ubah sesuai nama folder kamu
output_folder = 'foto_resize'
size = (300, 300)  # Ubah ke (500, 500) kalau mau

# Bikin folder output kalau belum ada
os.makedirs(output_folder, exist_ok=True)

# Proses semua gambar di folder input
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize(size)
        img.save(os.path.join(output_folder, filename))

print("Resize selesai, baka~")
