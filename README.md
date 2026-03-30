<div align="center">

# 🎥 Motion Detector

**A lightweight, real-time motion detection app powered by Python & OpenCV**
 
Detects movement through your webcam in real time using frame differencing —
no deep learning, no heavy dependencies, just pure OpenCV.

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Controls](#-controls)
- [How It Works](#-how-it-works)
- [Sensitivity Tuning](#-sensitivity-tuning)
- [Enabling Screenshots](#-enabling-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Possible Enhancements](#-possible-enhancements)

---

## 🧭 Overview

Motion Detector is a simple yet effective real-time surveillance tool that uses your device's webcam to detect motion using **frame differencing** — comparing consecutive frames to identify pixel-level changes. When movement is detected, it draws bounding boxes around the moving regions and overlays a live status indicator on screen.

No internet connection, no cloud, no GPU — runs entirely on your local machine.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🟢 Real-time detection | Processes webcam feed frame-by-frame |
| 📦 Bounding boxes | Highlights motion regions with green rectangles |
| 🪟 Dual window view | Live feed + binary threshold mask side by side |
| 🏷️ Status overlay | On-screen `Motion` / `No Motion` indicator |
| 📸 Screenshot capture | Save timestamped snapshots with a keypress |
| 🔁 Mirrored feed | Selfie-style horizontal flip for natural interaction |
| ⚡ Lightweight | No ML models — runs on any standard laptop webcam |

---

## 🛠️ Requirements

- Python **3.7 or higher**
- OpenCV library

```bash
pip install opencv-python
```

> **Note:** No GPU or special hardware is required. A standard built-in webcam works perfectly.

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/motion-detector.git

# 2. Navigate into the project folder
cd motion-detector

# 3. Install the required dependency
pip install opencv-python

# 4. Run the script
python motion_detector.py
```

---

## ▶️ Usage

```bash
python motion_detector.py
```

Once started:
- **Two windows** will open — the live camera feed and a threshold mask view.
- Any movement in front of the camera will be **highlighted with a green box**.
- The top-left corner shows the current detection status in real time.
- Press `Q` to exit cleanly.

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| `Q` | Quit the application |
| `S` | Save a screenshot to the output folder *(requires setup — see below)* |

---

## ⚙️ How It Works

The detector follows a simple 6-step pipeline on every frame:

```
📷 Webcam Frame
      │
      ▼
🔲 Grayscale Conversion
      │
      ▼
🌫️  Gaussian Blur  (reduces noise)
      │
      ▼
📊 Frame Difference  (current vs previous)
      │
      ▼
⬛ Binary Threshold  (isolates changed pixels)
      │
      ▼
🔍 Contour Detection  (finds motion regions)
      │
      ▼
🟩 Draw Bounding Boxes on Live Feed
```

**Why Gaussian Blur?**
Blurring before differencing smooths out minor pixel noise (lighting flickers, sensor grain) so only genuine movement triggers a detection.

**Why Dilate?**
Dilation expands the detected white regions in the threshold mask, filling small gaps so nearby motion blobs merge into one clean contour instead of many tiny ones.

---

## 🎛️ Sensitivity Tuning

Two parameters let you control how sensitive the detector is:

### 1. Pixel Change Threshold
```python
_, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)
#                               ^^
#                        Change this value
```
| Value | Effect |
|-------|--------|
| Lower (e.g. `5`) | More sensitive — detects subtle movements like a hand wave |
| Higher (e.g. `30`) | Less sensitive — ignores minor lighting shifts or distant motion |

### 2. Minimum Contour Area
```python
if cv2.contourArea(contour) < 500:
    continue
#                    ^^^
#             Change this value
```
| Value | Effect |
|-------|--------|
| Lower (e.g. `100`) | Detects small objects like a finger or insect |
| Higher (e.g. `2000`) | Only triggers for large movements like a full body |

> 💡 **Tip:** In bright or stable environments, keep defaults. In windy, flickering, or outdoor settings, raise both values to avoid false positives.

---

## 📸 Enabling Screenshots

Screenshot saving is disabled by default. To enable it:

**Step 1 —** Uncomment these two lines near the top of the script:

```python
folder_name = "motion_screenshots"
os.makedirs(folder_name, exist_ok=True)
```

**Step 2 —** Press `S` while the app is running to save a snapshot.

Screenshots are saved with timestamps in this format:
```
motion_screenshots/screenshot_20240315_142305.png
```

---

## 🔧 Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `Camera could not be opened` | Wrong camera index or webcam in use | Change `VideoCapture(0)` to `VideoCapture(1)` or close other apps using the camera |
| `Could not read first frame` | Camera initialised too slowly | Add `time.sleep(1)` after `cap = cv2.VideoCapture(0)` |
| Too many false detections | Background noise or lighting changes | Increase threshold value and minimum contour area |
| Motion not detected | Movement too slow or too far | Lower threshold value and minimum contour area |
| Screenshot not saving | Folder setup not enabled | Uncomment the `folder_name` lines (see above) |
| Laggy/choppy video | Low system resources | Increase `cv2.waitKey(30)` to `60` to reduce frame rate |

---

## 🔮 Possible Enhancements

- **Auto-save on motion** — Automatically capture screenshots when movement is detected rather than manually
- **Motion logging** — Write detection events with timestamps to a `.csv` file for audit trails
- **Email / SMS alerts** — Send a notification when motion is detected using `smtplib` or Twilio
- **ROI (Region of Interest)** — Monitor only a specific zone of the frame rather than the full image
- **Better background subtraction** — Replace frame differencing with `cv2.createBackgroundSubtractorMOG2()` for more robust detection
- **Multi-camera support** — Run multiple `VideoCapture` streams simultaneously
- **Recording** — Save a video clip of the motion event using `cv2.VideoWriter`

---
  

Made with ❤️ using Python & OpenCV

</div>
