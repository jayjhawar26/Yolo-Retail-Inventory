# YOLO Retail Inventory Tracker - Complete Setup Guide

## Overview

This guide provides step-by-step instructions for setting up the YOLO Retail Inventory Tracker project from scratch. It covers both the initial setup and ongoing development workflow.

## System Requirements

- **OS**: Windows 10/11, macOS 10.14+, or Ubuntu 18.04+
- **Python**: 3.7 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: At least 5GB free space for dependencies and datasets
- **GPU** (Optional): NVIDIA GPU with CUDA support for faster inference

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/YOLO-Retail-Inventory-Tracker.git
cd YOLO-Retail-Inventory-Tracker
```

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS/Linux

```bash
python3 -m venv venv
```

## Step 3: Activate Virtual Environment

### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

**Verification**: You should see `(venv)` prefix in your terminal prompt.

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- OpenCV for image processing
- PyTorch for deep learning
- NumPy for numerical operations
- And other supporting libraries

**Installation time**: 5-15 minutes depending on internet speed and hardware.

## Step 5: Verify Installation

### Test Camera Module

```bash
python camera_test.py
```

**Expected output:**
- A window opens showing your webcam feed
- Frame counter displays in the top-left corner
- Press `q` to exit

### Test Python Imports

```bash
python -c "import cv2; import torch; print('✓ All dependencies installed correctly')"
```

## Directory Structure

After setup, your project directory should look like:

```
YOLO-Retail-Inventory-Tracker/
├── .git/                       # Git repository metadata
├── venv/                       # Virtual environment (do not commit)
├── reference_repo/             # Reference YOLOv5 implementation
│   ├── detect.py
│   ├── train.py
│   ├── models/
│   └── ...
├── camera_test.py              # Phase 1: Camera feed module
├── requirements.txt            # Dependency list
├── .gitignore                  # Git configuration
├── README.md                   # Project overview
├── SETUP_GUIDE.md             # This file
└── DEVELOPMENT.md             # Development guidelines
```

## Troubleshooting

### Virtual Environment Issues

**Problem**: `(venv)` prefix not showing after activation

**Solution**:
```bash
# Deactivate and reactivate
deactivate
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # macOS/Linux
```

### Dependency Installation Fails

**Problem**: `pip install -r requirements.txt` fails

**Solutions**:
1. Upgrade pip:
   ```bash
   python -m pip install --upgrade pip
   ```

2. Install packages individually:
   ```bash
   pip install numpy
   pip install opencv-python
   pip install torch torchvision
   ```

3. Use cached wheels:
   ```bash
   pip install -r requirements.txt --cache-dir ~/.pip-cache
   ```

### Camera Not Found

**Problem**: `camera_test.py` says "Could not open webcam"

**Solutions**:
1. Check if camera is in use by another app (Zoom, Teams, etc.)
2. Restart your computer
3. Check camera drivers are up to date
4. Try a different USB port (if external camera)
5. Run: `python camera_test.py` with camera index:
   ```bash
   # Try different camera indices (0, 1, 2, etc.)
   ```

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'cv2'`

**Solution**:
1. Ensure virtual environment is activated: `where python` should show venv path
2. Reinstall the package:
   ```bash
   pip uninstall opencv-python -y
   pip install opencv-python
   ```

## Development Workflow

### Daily Setup

```bash
cd YOLO-Retail-Inventory-Tracker
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
```

### Making Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes and test locally

3. Commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. Push to remote:
   ```bash
   git push origin feature/my-feature
   ```

5. Create Pull Request on GitHub

### Deactivating Virtual Environment

```bash
deactivate
```

## Updating Dependencies

To update all packages to their latest compatible versions:

```bash
pip install --upgrade -r requirements.txt
```

To check for outdated packages:

```bash
pip list --outdated
```

## Reference Repository

The `reference_repo/` folder contains the YOLOv5 Retail Detection project. To explore it:

```bash
cd reference_repo
ls -la  # or dir on Windows
```

Key files to review:
- `detect.py` - Inference script
- `train.py` - Training script
- `models/` - Model architecture files
- `utils/` - Utility functions

## Next Steps

1. **Phase 1 Complete**: You have successfully set up the development environment
2. **Phase 2**: Integrate YOLOv5 with the camera module
3. **Phase 3**: Implement object tracking and inventory database
4. **Phase 4**: Build API and web dashboard

## Getting Help

- **Documentation**: Check README.md and DEVELOPMENT.md
- **Issues**: Search existing GitHub issues or create a new one
- **Team**: Ask in team Slack/Discord channel

## Advanced Configuration

### GPU Support (NVIDIA)

To enable GPU acceleration:

1. Install NVIDIA GPU drivers
2. Install CUDA Toolkit
3. Install cuDNN
4. Install GPU-enabled PyTorch:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

### IDE Setup

#### VS Code
1. Open the project folder
2. Install Python extension
3. Select interpreter: `.\venv\Scripts\python.exe`
4. Install Pylint for linting

#### PyCharm
1. Open the project
2. Go to Settings → Project → Python Interpreter
3. Add interpreter from venv path

## Tips for Success

- Always work in a feature branch
- Test your code locally before pushing
- Keep commits focused and descriptive
- Use `.gitignore` to prevent committing large files
- Regularly pull from main branch to stay updated
- Ask questions in team channels if stuck

---

**Last Updated**: May 2026  
**Version**: 1.0  
**Maintained by**: YOLO Retail Team
