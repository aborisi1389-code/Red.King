# 👑 Red King - Intelligent Fire Detection System

> 🚧 **PROJECT STATUS: PRE-RELEASE / BETA VERSION (v0.1)** 🚧
> 
> **Please Note:** This is an early, experimental version of the Red King project. 
> **Currently, the system ONLY detects fire based on color analysis.** Features like motion detection, sound recognition, SMS integration, and database logging are planned for future releases and are NOT included in this version.

**Red King** is a lightweight, offline computer vision system designed to detect fire in video streams and trigger instant audio alerts. Built entirely in Python, this project was created to demonstrate that powerful security systems can be developed with zero budget, using basic hardware and open-source tools.

It is designed to run on low-spec machines (like an old Intel i3 with 8GB RAM) and operates completely offline (Air-Gapped), ensuring maximum security and privacy for environments like schools or small offices.

## ✨ Current Features (v0.1)
*   **Fire Color Detection (Only):** Uses HSV color space filtering to detect the distinct colors of fire (Red, Orange, Bright Yellow). *Note: Motion and sound detection are not yet implemented.*
*   **Contour Bounding Boxes:** Draws a red bounding box around the detected fire in real-time.
*   **Audio Alarm System:** 
    *   *Windows:* Uses `winsound` for a loud, siren-like beep.
    *   *Linux:* Uses `spd-say` for a robotic voice alert ("Fire detected in the school!").
*   **Offline & Lightweight:** No internet connection required. Optimized to run efficiently on older CPUs by resizing frames before processing.

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed and install the required libraries:

```bash
pip install opencv-python numpy
