import cv2

def descale_image(input_image):
    # Get the original image dimensions
    height, width = input_image.shape[:2]
    descaled_image = input_image

    critical_pixel = 2048
    # Ideal value = 2048 since using GPU it takes about 12 GBs of VRAM and works on CPU as well without being too slow
    # >=2560, 3072, 4096 gives CUDA OOM Error on GPU and gets killed automatically on CPU
    # Since, 2048 works fine, upscaling is only required by a scale factor of ~2x and not (~4x)
    descale_factor = min(critical_pixel/height, critical_pixel/width)

    print(f'descale_factor = {descale_factor}')

    # Calculate the new dimensions while maintaining the aspect ratio
    # Descale only when descale factor is less than 1
    if descale_factor < 1:
        width = int(width * descale_factor)
        height = int(height * descale_factor)
        # Resize the image using OpenCV
        descaled_image = cv2.resize(input_image, (width, height), interpolation=cv2.INTER_AREA)

    return descaled_image
