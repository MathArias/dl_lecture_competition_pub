import os
import shutil
from concurrent.futures import ThreadPoolExecutor

src_dir = "/content/drive/MyDrive/Colab Notebooks/DLBasics2024_colab/FinalProject/VQA/dl_lecture_competition_pub/data"
dst_dir = "/content/data"

os.makedirs(dst_dir, exist_ok=True)

files_to_copy = []
for root, _, files in os.walk(src_dir):
  for file in files:
    src_file = os.path.join(root, file)
    dst_file = os.path.join(dst_dir, os.path.relpath(src_file,src_dir))
    files_to_copy.append((src_file, dst_file))

def copy_file(src_dst):
  src_file, dst_file = src_dst
  dst_file_dir = os.path.dirname(dst_file)
  os.makedirs(dst_file_dir, exist_ok=True)
  try:
    shutil.copy2(src_file, dst_file)
  except Exception as e:
    print(f"Error copying {src_file} to {dst_file}: {e}")

with ThreadPoolExecutor(max_workers=24) as executor:
  executor.map(copy_file, files_to_copy)

copied_files = [os.path.join(root, file) for root, _, files in os.walk(dst_dir) for file in files]
missing_files = [src for src, dst in files_to_copy if dst not in copied_files]

if missing_files:
  print(f"Missing files: {missing_files}")
else:
  print("All files copied successfully.")