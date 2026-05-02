# YOLO Retail Inventory Tracker - Development Guide

## Quick Start

```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate    # macOS/Linux

# Run camera test
python camera_test.py

# Deactivate when done
deactivate
```

## Project Structure

```
YOLO-Retail-Inventory-Tracker/
├── reference_repo/          # YOLOv5 reference implementation (READ-ONLY)
├── venv/                    # Python virtual environment (do NOT commit)
├── .git/                    # Git repository
├── .gitignore               # Files to ignore in git
├── requirements.txt         # Python dependencies
├── camera_test.py           # Phase 1: Camera feed module
├── README.md                # Project overview
├── SETUP_GUIDE.md          # Setup instructions
├── DEVELOPMENT.md          # This file
```

## File Descriptions

### camera_test.py
- **Purpose**: Capture and display live camera feed
- **Status**: Phase 1 (Complete)
- **Usage**: `python camera_test.py`
- **Features**:
  - Real-time webcam display
  - Frame counter
  - Screenshot capture (press 'c')
  - Error handling

### requirements.txt
- **Purpose**: Python package dependencies
- **Maintained**: Yes
- **How to update**: 
  ```bash
  pip freeze > requirements_full.txt  # See all installed packages
  ```

### reference_repo/
- **Purpose**: Reference implementation from GitHub
- **Read-only**: Yes (do NOT modify)
- **Usage**: Study structure and implementation patterns
- **Key files**:
  - `detect.py` - Object detection script
  - `train.py` - Model training script
  - `models/` - Network architectures
  - `utils/` - Helper functions

## Git Workflow

### 1. Create Feature Branch

```bash
# Before starting work, pull latest changes
git pull origin main

# Create a new feature branch
git checkout -b feature/camera-improvements
```

Branch naming conventions:
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### 2. Make Changes

```bash
# Make your edits to files
# Test your changes
python camera_test.py

# Check what changed
git status
```

### 3. Commit Changes

```bash
# Stage specific files
git add camera_test.py
git add requirements.txt

# Or stage everything
git add .

# Commit with descriptive message
git commit -m "Add frame rate control to camera module"
```

Commit message format:
- First line: Short summary (50 characters max)
- Blank line
- Detailed explanation if needed

Examples:
```
Add frame rate limit to camera module
Fixes frame skipping issue on slower systems

Refactor camera initialization function
Improve error messages and add logging

Update README with GPU setup instructions
```

### 4. Push to Remote

```bash
git push origin feature/camera-improvements
```

### 5. Create Pull Request

1. Go to GitHub repository
2. Click "New Pull Request"
3. Select your branch
4. Add description of changes
5. Request review from team members
6. Address feedback and update as needed

### 6. Merge to Main

After approval, merge to main branch:
```bash
git checkout main
git pull origin main
git merge feature/camera-improvements
git push origin main
```

Then delete the feature branch:
```bash
git branch -d feature/camera-improvements
git push origin --delete feature/camera-improvements
```

## Code Style

### Python Conventions

Follow PEP 8 style guide:
- Use 4 spaces for indentation
- Max line length: 79 characters
- Use meaningful variable names
- Add docstrings to functions

Example:
```python
def process_frame(frame, threshold=0.5):
    """
    Process a single video frame for object detection.
    
    Args:
        frame (np.ndarray): Input image frame
        threshold (float): Detection confidence threshold
    
    Returns:
        list: Detected objects with bounding boxes
    """
    # Implementation here
    pass
```

### Comments

- Use comments to explain WHY, not WHAT
- Keep comments up-to-date with code
- Use docstrings for functions and classes

```python
# Good comment
# Skip frames if processing is slow to prevent lag
if processing_time > frame_interval:
    continue

# Bad comment
# Increment counter
count += 1
```

## Testing

### Manual Testing

```bash
# Test camera module
python camera_test.py

# Test imports
python -c "import cv2, torch; print('✓ OK')"

# Test with specific camera index
python -c "import cv2; cap=cv2.VideoCapture(1); print(cap.isOpened())"
```

### Logging

Add logging to your code:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting camera capture")
logger.warning("Camera resolution not optimal")
logger.error("Failed to open camera")
```

## Debugging

### Common Issues

**Issue**: Import errors
```bash
# Verify virtual environment is active
which python  # Should show venv path

# Reinstall packages
pip install -r requirements.txt --force-reinstall
```

**Issue**: Camera not working
```bash
# Test camera directly
python -c "import cv2; cap=cv2.VideoCapture(0); print('Opened:', cap.isOpened())"

# Try different camera index
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera found at index {i}")
    cap.release()
```

**Issue**: Memory leaks
```bash
# Check for unreleased resources
# Make sure to call cap.release() and cv2.destroyAllWindows()
```

### Using Python Debugger

```python
import pdb

# Set breakpoint
pdb.set_trace()

# Commands:
# n - next line
# s - step into
# c - continue
# l - list code
# p variable - print variable
# w - where (stack trace)
```

Or use VS Code debugger:
1. Create `.vscode/launch.json`
2. Set breakpoints by clicking line numbers
3. Press F5 to start debugging

## Performance Optimization

### Camera Capture

```python
# Set resolution to reduce processing
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Reduce frame rate if needed
cap.set(cv2.CAP_PROP_FPS, 15)

# Use hardware acceleration
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
```

### Memory Usage

```python
# Process frame in chunks
# Use grayscale when color not needed
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Release unused resources
del large_array
```

## Documentation

### Adding Comments

```python
def capture_frame(camera_index=0):
    """Capture a single frame from the specified camera.
    
    Args:
        camera_index (int): Index of camera device (default: 0)
    
    Returns:
        tuple: (success, frame) where frame is np.ndarray or None
    
    Raises:
        RuntimeError: If camera cannot be opened
    """
```

### Updating README

Keep README updated with:
- Installation steps
- Usage examples
- Project status
- Known issues
- Contact information

## Useful Commands

```bash
# See project structure
tree /L 2

# Check git status
git status

# See commit history
git log --oneline -10

# See changes to a file
git diff camera_test.py

# Undo uncommitted changes
git checkout -- camera_test.py

# See which branch you're on
git branch

# Clean up unused branches
git branch -d feature/old-feature
```

## Resources

- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

## Team Communication

- **Issues**: Use GitHub Issues to report bugs and suggest features
- **Discussions**: Use GitHub Discussions for questions
- **Pull Requests**: Use PRs for code review and feedback
- **Team Channel**: Use Slack/Discord for quick questions

## Checklist Before Pushing

- [ ] Code tested locally
- [ ] No debug print statements left
- [ ] Comments added for complex logic
- [ ] Requirements.txt updated if new packages added
- [ ] No large files committed (check .gitignore)
- [ ] Commit message is descriptive
- [ ] Branch name follows convention

## Support

Having issues? Check these resources:
1. Project README
2. SETUP_GUIDE.md
3. GitHub Issues
4. Ask in team channel

---

**Last Updated**: May 2026  
**Version**: 1.0
