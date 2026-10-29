# Red.King
An offline, lightweight Python-based computer vision system for real-time fire detection and audio alerting. Designed for zero-budget school security.
# 👑 Red King - Intelligent Fire Detection System

**Red King** is a lightweight, offline computer vision system designed to detect fire in video streams and trigger instant audio alerts. Built entirely in Python, this project was created to demonstrate that powerful security systems can be developed with zero budget, using basic hardware and open-source tools.

It is designed to run on low-spec machines (like an old Intel i3 with 8GB RAM) and operates completely offline (Air-Gapped), ensuring maximum security and privacy for environments like schools or small offices.

## ✨ Features

*   **Fire Color Detection:** Uses HSV color space filtering to detect the distinct colors of fire (Red, Orange, Bright Yellow).
*   **Contour Bounding Boxes:** Draws a red bounding box around the detected fire in real-time.
*   **Audio Alarm System:** 
    *   *Windows:* Uses `winsound` for a loud, siren-like beep.
    *   *Linux:* Uses `spd-say` for a robotic voice alert ("Fire detected in the school!").
*   **Offline & Lightweight:** No internet connection required. Optimized to run efficiently on older CPUs by resizing frames before processing.

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed and install the required libraries:

```bash
pip install opencv-python numpy
