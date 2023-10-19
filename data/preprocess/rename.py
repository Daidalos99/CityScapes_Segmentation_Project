import os

folder_path = "./data/train/augmentation/labelIds"
#folder_path = "./val/labelIds"
#folder_path = "./val/leftImg"

new_prefix = ""  # Specify the new prefix for the filenames

counter = 5951
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        new_filename = f"{new_prefix}{counter:05d}.png"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1