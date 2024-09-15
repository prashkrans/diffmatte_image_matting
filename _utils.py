import os
import json

with open('config.json') as file:
    config = json.load(file)

INPUT_DIR = config['INPUT_DIR']
DESCALED_DIR = config['DESCALED_DIR']
TRIMAP_DIR = config['TRIMAP_DIR']
ALPHA_MATTE_DIR = config['ALPHA_MATTE_DIR']
OUTPUT_DIR = config['OUTPUT_DIR']
CONFIG_FILE_PATH = config['CONFIG_FILE_PATH']
CHECKPOINT_PATH = config['CHECKPOINT_PATH']

os.makedirs(DESCALED_DIR, exist_ok=True)
os.makedirs(TRIMAP_DIR, exist_ok=True)
os.makedirs(ALPHA_MATTE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_image_names_with_ext_from_folder(folder_path):
    # List files in the directory
    files = os.listdir(folder_path)
    image_names_with_ext = []

    for file in files:
        # Check if the file is a .jpg or .png file
        if file.lower().endswith(('.jpg', '.png', 'jpeg')):
            image_names_with_ext.append(file)

    return image_names_with_ext

def is_image_file(filename):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    return os.path.splitext(filename)[1].lower() in image_extensions

def clear_image_files(src_dir):
    for filename in os.listdir(src_dir):
        if is_image_file(filename):
            file_path = os.path.join(src_dir, filename)
            try:
                os.unlink(file_path)
                print(f'Deleted: {file_path}')
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')