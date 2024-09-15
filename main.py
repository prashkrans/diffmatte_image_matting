import ttkbootstrap as ttk
from _1_upload_images import ImageUploader
from _3_generate_trimap import generate_trimap
from _4_generate_alpha_matte import generate_alpha_matte
from _5_crop_using_alpha_matte import create_cropped_image
from _utils import INPUT_DIR, OUTPUT_DIR, TRIMAP_DIR, DESCALED_DIR, ALPHA_MATTE_DIR, clear_image_files
from _6_download_images import ImageDownloader

def process_images():
    generate_trimap(INPUT_DIR, DESCALED_DIR, TRIMAP_DIR)
    generate_alpha_matte(INPUT_DIR, DESCALED_DIR, TRIMAP_DIR, ALPHA_MATTE_DIR)
    create_cropped_image(INPUT_DIR, DESCALED_DIR, ALPHA_MATTE_DIR, OUTPUT_DIR)

if __name__ == "__main__":
    dirs = [INPUT_DIR, OUTPUT_DIR, TRIMAP_DIR, DESCALED_DIR, ALPHA_MATTE_DIR]
    for dir in dirs:
        clear_image_files(dir)

    # Initiate root for uploading images
    root = ttk.Window()
    uploader_app = ImageUploader(root)
    root.mainloop()  # Run the uploader window

    # Process images after upload
    process_images()

    # Use the same root for downloading image
    downloader_app = ImageDownloader(root)

    root.deiconify()  # Show the window
    root.mainloop()  # Run the downloader window