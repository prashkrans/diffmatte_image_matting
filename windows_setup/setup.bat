@echo off
setlocal enabledelayedexpansion

:: Remove existing diffmatte_image_matting directory if it exists
if exist diffmatte_image_matting (
    echo Removing existing diffmatte_image_matting directory...
    rmdir /s /q diffmatte_image_matting
    if %errorLevel% neq 0 (
        echo Failed to remove existing diffmatte_image_matting directory.
        pause
        exit /b 1
    )
)

:: Clone the repository
echo Cloning the repository...
git clone https://github.com/prashkrans/diffmatte_image_matting.git
if %errorLevel% neq 0 (
    echo Failed to clone the repository.
    pause
    exit /b 1
)
cd diffmatte_image_matting

:: Create and activate virtual environment
echo Creating and activating virtual environment...
python -m venv env_diff
if %errorLevel% neq 0 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)
call env_diff\Scripts\activate.bat

:: Install requirements and gdown
echo Installing requirements...
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
pip install -r requirements.txt
pip install gdown
if %errorLevel% neq 0 (
    echo Failed to install requirements.
    pause
    exit /b 1
)

:: Download the model using gdown
echo Downloading the diffmatte checkpoint model...
gdown "https://drive.google.com/uc?id=1NIn-tKtW3zhi2vK3OgOTiiHrOIXuHIZo" -O .\checkpoints\DiffMatte_ViTS_Com_1024.pth
if %ERRORLEVEL% neq 0 (
    echo Failed to download the model.
    pause
    exit /b 1
)

echo Setup complete!
pause
