# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install virtual environment (optional but preferred)
python -m pip install virtualenv
python -m virtualenv .venv
.venv\Scripts\activate  # For Windows
# source .venv/bin/activate  # For macOS/Linux

# Install required libraries
pip install pygame
pip install rembg
pip install numpy
pip install onnxruntime
pip install pillow


py 3.11.9
