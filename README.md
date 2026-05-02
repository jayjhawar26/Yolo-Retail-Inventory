# YOLO Retail Inventory Tracker

A computer vision system for real-time retail store item detection and inventory tracking using YOLOv5.

## Project Overview

This project aims to build an automated system that can detect and track retail items on store shelves in real-time using YOLO (You Only Look Once) deep learning model. The system will help retailers optimize inventory management and track product availability.

## Phase 1: Foundation & Camera Integration

### Status: In Progress

**Objectives:**
- ✅ Set up development environment with virtual environment
- ✅ Clone and explore reference implementation
- ✅ Create webcam feed capture module
- ✅ Prepare project structure for team collaboration

## Project Structure

```
YOLO-Retail-Inventory-Tracker/
├── reference_repo/           # Reference implementation from YOLOv5 retail project
├── venv/                     # Python virtual environment (do NOT commit)
├── camera_test.py            # Phase 1: Live camera feed module
├── requirements.txt          # Project dependencies
├── .gitignore               # Git configuration (prevents large files from being committed)
└── README.md                # This file
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Git
- Webcam or camera device

### Installation

1. **Clone this repository** (if you haven't already):
   ```bash
   git clone https://github.com/jayjhawar26/Yolo-Retail-Inventory/
   cd YOLO-Retail-Inventory-Tracker
   ```

2. **Create a virtual environment**:
   
   **Windows:**
   ```bash
   python -m venv venv
   ```
   
   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   
   **Windows:**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
   
   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - OpenCV for image processing
   - PyTorch and TorchVision for deep learning
   - NumPy, SciPy for numerical computations
   - Matplotlib for visualization
   - And other supporting libraries

## Phase 1 Testing: Camera Module

To test the camera feed capture module:

```bash
# Make sure your virtual environment is activated
python camera_test.py
```

### Expected Behavior

- A window titled "YOLO Retail: Live Camera Feed Test" will open
- Your webcam feed will display in real-time
- Frame count will be displayed in the top-left corner
- Press `q` to quit the application
- Press `c` to capture a screenshot (saved as `camera_capture_<frame_num>.jpg`)

### Troubleshooting

**Camera not found:**
- Verify your webcam is connected
- Check that no other application is using the camera
- Try updating your camera drivers

**Module import errors:**
- Ensure virtual environment is activated: `which python` should point to your venv
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## Important: .gitignore

The `.gitignore` file prevents large files from being committed to GitHub:
- Model weights (*.pt, *.onnx)
- Datasets (datasets/, SKU-110K/)
- Virtual environment (venv/)
- Python cache files

**Do NOT** modify or remove the `.gitignore` file.

## Team Collaboration

### Adding Collaborators to GitHub

1. Go to Settings → Collaborators → Add people
2. Search for each team member's GitHub username
3. Select the appropriate permission level (usually "Collaborator")

### Git Workflow

1. Always work in a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. Push to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request for code review

## Dependencies Overview

| Package | Purpose |
|---------|---------|
| opencv-python | Image capture and processing |
| torch | Deep learning framework |
| torchvision | Vision models and utilities |
| numpy | Numerical operations |
| matplotlib | Data visualization |
| tensorboard | Training monitoring |
| PyYAML | Configuration files |
| scipy | Scientific computing |
| tqdm | Progress bars |

## Next Phases

### Phase 2: Model Integration
- Download YOLOv5 pre-trained weights
- Integrate YOLOv5 inference with camera feed
- Real-time object detection

### Phase 3: Inventory Tracking
- Implement object tracking across frames
- Track item movement and position
- Database for inventory storage

### Phase 4: Advanced Features
- Multi-camera support
- Performance optimization
- API endpoint development
- Web dashboard

## References

- [YOLOv5 GitHub Repository](https://github.com/ultralytics/yolov5)
- [Reference Project](https://github.com/shayanalibhatti/Retail-Store-Item-Detection-using-YOLOv5)
- [OpenCV Documentation](https://docs.opencv.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)

## Notes for Team

- **Do not** commit large model files or datasets
- Always use descriptive commit messages
- Test locally before pushing to main branch
- Create issues for bugs and feature requests
- Comment your code for clarity

## License

[To be determined by the team]

---

**Last Updated:** May 2026  
**Phase:** 1 - Foundation & Camera Integration  
**Team Lead:** Jay
