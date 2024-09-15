# Image Matting Python App using DiffMatte
- Given a single or multiple images, this tool allows the user to paint a trimap. Using the source images along with their trimaps, two results can be generated:
a. an image with the background removed, and
b. the alpha matte (Black and White Contour).
- A trimap is a grayscale image used in image segmentation or matting, where pixels are categorized into three regions: white (foreground), black (background), and grey (unknown). The white and black areas are clearly identified, while the grey regions are where the algorithm determines whether the pixel belongs to the foreground or background. This helps in accurately separating objects from their backgrounds.
- The source image, along with the trimap, can then be fed into image matting models such as DiffMatte.
- Image matting is a technique used to accurately separate the foreground (such as a person or object) from the background in an image.
- This is particularly useful in tasks like creating transparent backgrounds, adding effects, or changing the background in photos and videos.
- DiffMatte can achieve precise and high-quality matting results, even in challenging scenarios like hair or semi-transparent objects.
- It is also slightly faster than ViTMatte and produce results upto 2048 pixels without any upscaling using a CPU itself

### Demo Video:
https://github.com/user-attachments/assets/0d57b137-3721-4e91-ab56-df076cc84f95

### Prerequisites:
- Python 3.10.14 (Might work with lower/higher versions as well)
- Miniconda for easier Python 3.10 environment setup
- Tkinter (Only for linux): `sudo apt install python3-tk`
- Tested with both NVIDIA CUDA and CPU. Works really well with CPU also. 
- Critical Resolution kept as 2048. For resolutions above 2048, more VRAM i.e. > 16GBs is required.
- Not sure about gcc and g++ errors, if encountered use `sudo apt install build-essential`

### Setup:
1. Clone the repo and move to the root dir.
```commandline
git clone https://github.com/prashkrans/diffmatte_image_matting.git
cd diffmatte_image_matting/
```
2. Download the [ViTS_1024 (Best Diffmatte Model)](https://drive.google.com/file/d/1NIn-tKtW3zhi2vK3OgOTiiHrOIXuHIZo/view?usp=drive_link)
and put it in checkpoints directory.
3. Create a python virtual environment.  

```
# a. Directly if python3.10 is installed
python3 -m venv env_diff
source env_diff/bin/activate
```
Or,

```
# b. Use miniconda to setup an enviroment with Python 3.10:
conda create --name env_diff python=3.10
conda activate env_diff
```
4. Install the requirements (Might take some time).   
```
sudo apt install python3-tk     # Only for linux
pip install -r requirements.txt
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
```
**Note:** There are no versions mentioned in requirements.txt as it fails to run when python versions are different like 3.10 or 3.11. 

### Usage:
1. Run `python3 main.py`.
2. Upload single or multiple images.
3. Paint trimaps sequentially for all the uploaded images.
4. Wait for the processing to complete after which two results would be obtained: a. an image with background removed and b. the alpha matte (Black and White Contour). These would also be saved at `output_dir` and `alpha_matte_dir` respectively, which could be downloaded at <date-time>_output_dir and <date_time>_alpha_matte_dir.

### Quick setup and usage for Windows: TODO 
**Note:**
- It has detectron 2 as a dependency which cannot be installed easily in Windows and needs a conda environment. 
- It also cannot be deployed using docker as it uses opencv image preview and user input for which an additional step of `VcXsrv Windows X Server` is required. 
- To be implented later.

### Trimap Keybinds:
1. Q or 1 => Grey Mask (Unknown Region)
2. E or 2 => White Mask (Foreground)
3. Up arrow or +/= => Increases the brush size
4. Down arrow or _/- => Decreases the brush size
5. Enter => Saves the trimap
6. Esc => Reverts all the changes

### Note:
- Descale option is used to avoid `CUDA OOM`.
- Dev Options: Feel free to play with `critical_pixel = 2048` in line 8 of `_2_descale_image.py` to have larger image resolution as output if having > 16GBs of GPU VRAM or use an upscaler.
- Currently, it doesn't support undo, so if the trimap gets messed up, you'd have to start over by pressing the `Esc` key.

### License:
This app and Diffmatte's model weights are released under the MIT License. See [LICENSE](LICENSE) for further details.

### Credits:
1. [DiffMatte Github](https://github.com/YihanHu-2022/DiffMatte)
2. [ViTMatte Github](https://github.com/hustvl/ViTMatte)


