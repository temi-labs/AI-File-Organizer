import os
import shutil

def move_file(base, file, folder_name):
    target = os.path.join(base, folder_name)

    if not os.path.exists(target):
        os.makedirs(target)

    shutil.move(os.path.join(base, file), os.path.join(target, file))
    print(f"Moved {file} → {folder_name}")
