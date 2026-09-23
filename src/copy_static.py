import os
import shutil

def copy_static(source: str, destination: str):
    if os.path.exists(source) and os.path.exists(destination):
        for item in os.listdir(destination):
            item_path = destination + "/" + item
            print(f"Checking object at {item_path}...")
            if os.path.isfile(item_path):
                print(f"Removing file at {item_path}")
                os.remove(item_path)
            else:
                print(f"Removing tree at {item_path}")
                shutil.rmtree(item_path)
        for item in os.listdir(source):
            item_path = source + "/" + item
            dest_path = destination + "/" + item
            print(f"Checking object at {item_path}...")
            if os.path.isfile(item_path):
                print(f"Copying file from {item_path} to {dest_path}")
                shutil.copy(item_path, dest_path)
            else:
                print(f"Copying directory from {item_path} to {dest_path}")
                shutil.copytree(item_path, dest_path)
