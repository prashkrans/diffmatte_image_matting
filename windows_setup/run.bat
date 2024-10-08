@echo off
setlocal

:: Change directory to vitmatte_image_matting
cd /d diffmatte_image_matting

:: Activate the virtual environment
call env_diff\Scripts\activate

:: Run main.py
echo Starting image matting...
python main.py
if %errorLevel% neq 0 (
    echo Failed to run main.py.
    pause
    exit /b 1
)

endlocal
