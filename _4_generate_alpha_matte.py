import cv2
import torch
from PIL import Image
from re import findall
from os.path import join as opj
from torchvision.transforms import functional as F
from detectron2.engine import default_argument_parser
from detectron2.config import LazyConfig, instantiate
from detectron2.checkpoint import DetectionCheckpointer

from _utils import get_image_names_with_ext_from_folder, CONFIG_FILE_PATH, CHECKPOINT_PATH


def generate_alpha_matte_for_an_image(model, image_data, alpha_matte_path):
    """
    Generates the alpha matte for an image.
    """
    output = model(image_data)
    output = cv2.cvtColor(output, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(opj(alpha_matte_path), output)


def init_model(model, checkpoint, device, sample_strategy):
    """
    Initializes the model.
    """
    cfg = LazyConfig.load(model)
    if sample_strategy is not None:
        cfg.difmatte.args["use_ddim"] = True if "ddim" in sample_strategy else False
        cfg.diffusion.steps = int(findall(r"\d+", sample_strategy)[0])

    model = instantiate(cfg.model)
    diffusion = instantiate(cfg.diffusion)
    cfg.difmatte.model = model
    cfg.difmatte.diffusion = diffusion
    difmatte = instantiate(cfg.difmatte)
    difmatte.to(device)
    difmatte.eval()
    DetectionCheckpointer(difmatte).load(checkpoint)

    return difmatte


def get_data(image_dir, trimap_dir):
    """
    Gets the data of an image.
    """
    image = Image.open(image_dir).convert('RGB')
    image = F.to_tensor(image).unsqueeze(0)
    trimap = Image.open(trimap_dir).convert('L')
    trimap = F.to_tensor(trimap).unsqueeze(0)

    # force tri-values in trimap
    trimap[trimap > 0.9] = 1.00000
    trimap[(trimap >= 0.1) & (trimap <= 0.9)] = 0.50000
    trimap[trimap < 0.1] = 0.00000

    return {
        'image': image,
        'trimap': trimap
    }

def generate_alpha_matte(input_dir, descaled_dir, trimap_dir, alpha_matte_dir):
    print('Initiating the process to generate the alpha matte using DiffMatte')
    image_names_with_ext = get_image_names_with_ext_from_folder(input_dir)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    # device = "cpu" # Both GPU and CPU supports for a critical resolution of 2048
    sample_strategy = "ddim10"
    model = init_model(CONFIG_FILE_PATH, CHECKPOINT_PATH, device, sample_strategy)

    for image_name_with_ext in image_names_with_ext:
        image_name = image_name_with_ext.split('.')[0]
        descaled_img_name = f'{image_name}_desc.png'
        trimap_name = f'{image_name}_trimap.png'
        alpha_matte_name = f'{image_name}_alpha.png'

        descaled_img_path = f'{descaled_dir}/{descaled_img_name}'
        trimap_path = f'{trimap_dir}/{trimap_name}'
        alpha_matte_path = f'{alpha_matte_dir}/{alpha_matte_name}'

        print(f'Processing image: {image_name_with_ext} and its trimap: {trimap_name}')
        image_data = get_data(descaled_img_path, trimap_path)
        generate_alpha_matte_for_an_image(model, image_data, alpha_matte_path)
