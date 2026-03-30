**📄 Project Report**

**Real-Time Motion Detection System Using OpenCV**

**Subject:** Computer Vision / Python Programming  
**Technology Used:** Python, OpenCV  
**Project Type:** Individual Mini Project  

**📋 Table of Contents**

1.  [Introduction](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#1-introduction)
2.  [Objectives](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#2-objectives)
3.  [Tools and Technologies](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#3-tools-and-technologies)
4.  [System Requirements](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#4-system-requirements)
5.  [Working Principle](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#5-working-principle)
6.  [Algorithm](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#6-algorithm)
7.  [Module Description](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#7-module-description)
8.  [Code Explanation](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#8-code-explanation)
9.  [Output Description](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#9-output-description)
10.  [Sensitivity Parameters](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#10-sensitivity-parameters)
11.  [Advantages](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#11-advantages)
12.  [Limitations](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#12-limitations)
13.  [Future Scope](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#13-future-scope)
14.  [Conclusion](https://claude.ai/chat/51467ae6-2562-4b23-ad81-68542a144d3f#14-conclusion)

**1\. Introduction**

Motion detection is one of the fundamental and widely used applications in the field of computer vision. It refers to the process of detecting a change in the position of an object relative to its surroundings. With the growing need for security and surveillance systems, motion detection has become an essential technology in modern applications.

This project presents a **Real-Time Motion Detection System** built using Python and the OpenCV library. The system captures live video from a webcam and detects any motion by comparing consecutive frames. When motion is detected, it draws bounding boxes around the moving regions and displays a status indicator on the screen.

Unlike complex deep learning-based solutions, this system uses a classical computer vision technique called **Frame Differencing**, which is computationally lightweight and can run efficiently on any standard laptop without requiring a GPU.

**2\. Objectives**

The primary objectives of this project are:

*   To develop a real-time motion detection system using Python and OpenCV.
*   To apply image processing techniques such as grayscale conversion, Gaussian blurring, thresholding, dilation, and contour detection.
*   To visually highlight detected motion regions using bounding boxes on the live video feed.
*   To provide an intuitive dual-window display showing both the live feed and the binary threshold mask.
*   To allow manual screenshot capture with timestamped filenames.
*   To build a lightweight system that works without any machine learning models or GPU requirements.

**3\. Tools and Technologies**

| Component | Details |
| --- | --- |
| Programming Language | Python 3.7+ |
| Core Library | OpenCV (cv2) |
| Additional Modules | os, datetime (Python Standard Library) |
| Input Device | Webcam (built-in or external) |
| IDE | VS Code / PyCharm / Any Python IDE |
| Platform | Windows / macOS / Linux |

**Why OpenCV?**

OpenCV (Open Source Computer Vision Library) is the industry-standard library for real-time computer vision tasks. It provides:

*   Highly optimised C++ backend with a Python interface
*   Built-in functions for image filtering, thresholding, contour detection, and drawing
*   Cross-platform compatibility
*   Active community and extensive documentation

**4\. System Requirements**

**Hardware Requirements**

| Component | Minimum Requirement |
| --- | --- |
| Processor | Intel Core i3 or equivalent |
| RAM | 4 GB |
| Webcam | 720p built-in or USB webcam |
| Storage | 100 MB free space |

**Software Requirements**

| Component | Requirement |
| --- | --- |
| Operating System | Windows 10 / macOS 10.14 / Ubuntu 18.04 or above |
| Python | Version 3.7 or higher |
| OpenCV | pip install opencv-python |

**5\. Working Principle**

The system is based on the **Frame Differencing** technique, one of the simplest and most effective methods for motion detection in video streams.

**Core Idea**

Every video is a sequence of frames captured at a fixed rate. If there is no motion in the scene, consecutive frames will look identical. If something moves, the pixel values in those regions will change between frames. By computing the difference between the current frame and the previous frame, we can isolate the regions where motion has occurred.

**Step-by-Step Flow**

┌─────────────────────────────────────────────┐

│ WEBCAM CAPTURES FRAME │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Convert to Grayscale + Gaussian Blur │

│ (Noise Reduction Step) │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Compute Absolute Difference Between │

│ Current Frame & Previous Frame │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Apply Binary Threshold to Difference │

│ (Isolate significantly changed pixels) │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Dilate Threshold Mask │

│ (Fill gaps, merge nearby blobs) │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Find Contours in Threshold Mask │

│ Filter by Minimum Area (remove noise) │

└────────────────────┬────────────────────────┘

│

▼

┌─────────────────────────────────────────────┐

│ Draw Bounding Boxes + Status Text │

│ on Live Frame and Display Output │

└─────────────────────────────────────────────┘

**6\. Algorithm**

START

1\. Initialize webcam using VideoCapture(0)

2\. Read the first frame as the reference (previous frame)

3\. Flip the frame horizontally (mirror effect)

4\. Convert to grayscale and apply Gaussian blur

LOOP (for each subsequent frame):

a. Read the current frame from the webcam

b. Flip the current frame horizontally

c. Convert to grayscale

d. Apply Gaussian blur with kernel size (11, 11)

e. Compute absolute difference between current and previous grayscale frame

f. Apply binary threshold (value: 15) to the difference image

g. Apply dilation with 2 iterations to fill gaps

h. Find external contours in the dilated threshold image

FOR each contour:

\- If contour area < 500 pixels → skip (noise)

\- Else → set motion\_detected = True

\- Compute bounding rectangle

\- Draw green rectangle on the live frame

\- Display "Motion Detected" label near bounding box

i. Display "Status: Motion" or "Status: No Motion" on frame

j. Show live feed window and threshold window

k. Wait for keypress (30ms delay)

\- If 'Q' → break loop and exit

\- If 'S' → save screenshot with timestamp

l. Update previous frame = current frame

END LOOP

Release webcam

Destroy all windows

END

**7\. Module Description**

**7.1 cv2 — OpenCV**

The core library powering the entire application. Key functions used:

| Function | Purpose |
| --- | --- |
| cv2.VideoCapture() | Access and read webcam stream |
| cv2.flip() | Mirror the frame horizontally |
| cv2.cvtColor() | Convert BGR frame to grayscale |
| cv2.GaussianBlur() | Smooth the frame to reduce noise |
| cv2.absdiff() | Compute pixel-wise absolute difference |
| cv2.threshold() | Apply binary threshold to difference image |
| cv2.dilate() | Expand white regions in threshold mask |
| cv2.findContours() | Detect contours (boundaries of motion regions) |
| cv2.contourArea() | Calculate area of each contour |
| cv2.boundingRect() | Get bounding rectangle of a contour |
| cv2.rectangle() | Draw rectangle on frame |
| cv2.putText() | Render text on frame |
| cv2.imshow() | Display frame in a window |
| cv2.waitKey() | Wait for keyboard input |
| cv2.imwrite() | Save frame as image file |

**7.2 os — Operating System Interface**

Used to create the screenshot output directory programmatically with os.makedirs(), ensuring the folder exists before attempting to write files.

**7.3 datetime — Date and Time**

Used to generate unique, human-readable filenames for screenshots in the format:

screenshot\_YYYYMMDD\_HHMMSS.png

**8\. Code Explanation**

**8.1 Camera Initialization**

cap = cv2.VideoCapture(0)

Opens the default webcam (index 0). If a second camera is available, use index 1.

**8.2 Reading the First Frame**

ret, prev\_frame = cap.read()

prev\_frame = cv2.flip(prev\_frame, 1)

prev\_gray = cv2.cvtColor(prev\_frame, cv2.COLOR\_BGR2GRAY)

prev\_gray = cv2.GaussianBlur(prev\_gray, (11, 11), 0)

The first frame is captured to serve as the reference frame. It is flipped, converted to grayscale, and blurred to establish the baseline for comparison.

**8.3 Frame Differencing**

diff = cv2.absdiff(prev\_gray, gray)

Computes the absolute pixel-by-pixel difference between the current and previous preprocessed frames. Only regions with actual change will have high values.

**8.4 Thresholding**

\_, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH\_BINARY)

Converts the difference image into a binary (black and white) image. Any pixel with a difference greater than 15 becomes white (255), indicating motion. All others become black (0).

**8.5 Dilation**

thresh = cv2.dilate(thresh, None, iterations=2)

Expands white regions in the binary mask to fill small gaps and connect nearby blobs into unified contours, making bounding boxes more accurate.

**8.6 Contour Detection and Filtering**

contours, \_ = cv2.findContours(thresh, cv2.RETR\_EXTERNAL, cv2.CHAIN\_APPROX\_SIMPLE)

for contour in contours:

if cv2.contourArea(contour) < 500:

continue

Finds the outlines of white regions. Contours with an area smaller than 500 pixels are discarded as noise. Only significant motion triggers a detection.

**8.7 Bounding Box and Annotation**

x, y, w, h = cv2.boundingRect(contour)

cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.putText(frame, "Motion Detected", (x, y - 10), ...)

Draws a green rectangle around each detected motion region and adds a text label above it.

**9\. Output Description**

The application produces two real-time windows:

**Window 1 — Motion Detector (Live Feed)**

*   Displays the mirrored webcam feed
*   Green bounding boxes appear around detected motion areas
*   Label "Motion Detected" is shown near each box
*   Top-left shows "Status: Motion" (red) or "Status: No Motion" (blue)

**Window 2 — Threshold**

*   Displays the binary mask generated from frame differencing
*   White regions represent areas where motion was detected
*   Black regions represent static background
*   Useful for debugging sensitivity settings

**Screenshot Output**

When the S key is pressed (with folder setup enabled), a .png file is saved:

motion\_screenshots/

└── screenshot\_20240315\_142305.png

**10\. Sensitivity Parameters**

The system provides two tunable parameters that allow adjustment of detection sensitivity without modifying core logic:

**Parameter 1 — Threshold Value (15)**

cv2.threshold(diff, 15, 255, cv2.THRESH\_BINARY)

Controls how different a pixel must be to count as changed.

*   **Decrease** → More sensitive (picks up subtle changes)
*   **Increase** → Less sensitive (ignores minor lighting variation)

**Parameter 2 — Minimum Contour Area (500)**

if cv2.contourArea(contour) < 500:

Controls the minimum size of detected motion regions.

*   **Decrease** → Detects small objects (hands, insects)
*   **Increase** → Ignores small motion, detects only large movements

**11\. Advantages**

*   **No machine learning required** — Works entirely with classical image processing
*   **Lightweight** — Runs smoothly on standard hardware without a GPU
*   **Low dependency** — Only one external library (opencv-python) needed
*   **Real-time** — Processes video at near-native frame rates
*   **Cross-platform** — Works on Windows, macOS, and Linux without modification
*   **Easily tunable** — Sensitivity can be adjusted with just two values
*   **Beginner friendly** — Clean, readable code suitable for learning computer vision

**12\. Limitations**

*   **Lighting sensitivity** — Sudden lighting changes (e.g., lights turning on/off, sunlight shifts) can trigger false detections
*   **Static camera required** — Any camera movement is interpreted as motion
*   **Single camera only** — The current implementation supports one webcam at a time
*   **No persistence** — Motion events are not logged or recorded automatically
*   **Frame differencing limitation** — A slowly moving object may not be detected if it moves too gradually between frames
*   **No object classification** — The system detects that motion occurred but cannot identify what is moving (person, animal, vehicle, etc.)

**13\. Future Scope**

This project provides a solid foundation that can be extended in several meaningful directions:

| Enhancement | Description |
| --- | --- |
| Background Subtraction (MOG2) | Use cv2.createBackgroundSubtractorMOG2() for more robust detection against lighting changes |
| Object Classification | Integrate a pre-trained model (YOLO, MobileNet) to identify what is moving |
| Auto Screenshot on Motion | Automatically save screenshots when motion is detected without manual keypress |
| Motion Logging | Record detection events with timestamps to a .csv or .txt file |
| Email / SMS Alerts | Send real-time notifications via smtplib or Twilio API |
| Region of Interest (ROI) | Allow users to define a specific zone within the frame for focused monitoring |
| Video Recording | Save a short video clip when motion is triggered using cv2.VideoWriter |
| Multi-Camera Support | Handle multiple webcam streams simultaneously |
| Web Dashboard | Stream the output to a browser using Flask or FastAPI |
| Mobile App Integration | Send frames to a mobile app via WebSocket for remote monitoring |

**14\. Conclusion**

This project successfully demonstrates the implementation of a **Real-Time Motion Detection System** using Python and OpenCV. The system uses the frame differencing technique combined with Gaussian blurring, binary thresholding, dilation, and contour detection to reliably identify and highlight motion in a live webcam feed.

The application is lightweight, requires no machine learning models, and runs efficiently on standard hardware. It provides a clear dual-window output and allows real-time sensitivity tuning through two simple parameters.

This project serves as both a practical surveillance tool and an educational foundation in computer vision. The concepts explored here — frame differencing, thresholding, contour detection — are fundamental building blocks that appear in more advanced systems such as optical flow estimation, object tracking, and deep learning-based video analysis.

Overall, the project meets all its defined objectives and lays a strong groundwork for future enhancements such as automated alerting, object classification, and multi-camera monitoring.

_This report was prepared as part of a Python & Computer Vision mini project._