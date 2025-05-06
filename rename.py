import os

folder_path = "dataset/gedung-tabib"
label = "gedung-tabib"  # nama pendek yang kamu mau
ext = ".jpg"

for i, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(ext):
        new_name = f"{label}_{i+1}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")
