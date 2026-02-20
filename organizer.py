import os
import shutil
from config import IMAGE_EXT, VIDEO_EXT, DOC_EXT, CODE_EXT

def organize_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()

        if ext in IMAGE_EXT:
            move_file(folder_path, file, "Images")

        elif ext in VIDEO_EXT:
            move_file(folder_path, file, "Videos")

        elif ext in DOC_EXT:
            move_file(folder_path, file, "Documents")

        elif ext in CODE_EXT:
            move_file(folder_path, file, "Code")

def move_file(base, file, folder_name):
    target = os.path.join(base, folder_name)

    if not os.path.exists(target):
        os.makedirs(target)

    shutil.move(os.path.join(base, file), os.path.join(target, file))
    print(f"Moved {file} → {folder_name}")
