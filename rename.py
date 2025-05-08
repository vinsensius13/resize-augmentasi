import os

folder_path = "dataset-aug/rumah-hakim-aug"  # ganti dengan path folder kamu
label = "rumah-hakim"  # nama pendek yang kamu mau
ext = ".jpg"

for i, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(ext):
        new_name = f"{label}_{i+1}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("✅ Semua gambar udah di-rename. Baaakkaaaaaa! 😤💕")
