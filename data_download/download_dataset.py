import kagglehub
import os
import shutil

# Download dataset
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Path to dataset files:", path)

# move CSVs to a data folder
dest_dir = "../data"
os.makedirs(dest_dir, exist_ok=True)

for filename in os.listdir(path):
    if filename.endswith(".csv"):
        shutil.copy(os.path.join(path, filename), dest_dir)
