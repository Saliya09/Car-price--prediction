### `README.md`

```markdown
# Live Object Detection

This project implements real-time object detection using YOLOv5. It provides the flexibility to run the detection on video files or directly via a webcam.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Execution](#execution)
- [Changing Input Source](#changing-input-source)
- [Files](#files)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Download YOLOv5 Weights**: Weights will be downloaded automatically on the first run if the system is connected to the internet.

2. **Prepare Input**: Place your video in the `videos/` directory, or ensure your webcam is connected for live detection.

## Execution

### For Video Input
Run the detection on a video file:
```bash
python app.py
```

### For Webcam Input
Run the detection using a webcam:
```bash
python cam.py
```

## Changing Input Source

### Video Input
In `app.py`, modify the `cv2.VideoCapture` line to point to your video file:
```python
cap = cv2.VideoCapture('path/to/your/video.mp4')
```

### Camera Input
In `cam.py`, change the `cv2.VideoCapture` line if using a different camera:
```python
cap = cv2.VideoCapture(0)
```

## Files

- **`requirements.txt`**: Lists required Python packages.
- **`app.py`**: Runs detection on video files.
- **`cam.py`**: Runs detection using a webcam.
- **`camera.py`**: An additional script for camera management.

Feel free to contribute or report issues to enhance the project.

Happy coding!
```

This concise `README.md` will guide users through the setup and usage of your live object detection project, making it easy for others to understand and use.