import cv2
import numpy as np
import time
import threading
import platform
import os
#Fire detected in the school!
# ==========================================
# RED KING v1.0 - CORE VISION & AUDIO SYSTEM
# ==========================================
VIDEO_SOURCE = 'fire_test.mp4' 

print("=========================================")
print("[RED KING] Vision and Audio System Activated...")
print("=========================================")

last_alarm_time = 0
ALARM_COOLDOWN = 3.0  # Wait 3 seconds before triggering alarm again

def play_alarm():
    """Plays the alarm sound (Speech and Beep)"""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(2500, 800)
    else:
        # Linux: Use spd-say for voice alert and fallback to beep
        os.system("spd-say -w -r -3 'in dengear' &")
        print('\a') # Terminal beep as backup

# Open video source
cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    print(f"[-] Error: Cannot open file {VIDEO_SOURCE}.")
    exit()

# Get video FPS for natural playback speed
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or fps is None:
    fps = 30
delay = int(1000 / fps)

while True:
    ret, frame = cap.read()
    if not ret:
        print("[RED KING] End of video stream.")
        break

    # Resize for faster processing on older CPUs
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Optimized Fire Color Range (Covers Red, Orange, and bright Yellow)
    lower_fire = np.array([0, 60, 100])
    upper_fire = np.array([50, 255, 255])

    # Create mask and remove noise
    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 200: # Sensitivity threshold
            fire_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            
            # Put text
            cv2.putText(frame, "FIRE DETECTED!", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Trigger Alarm
    if fire_detected:
        current_time = time.time()
        if current_time - last_alarm_time > ALARM_COOLDOWN:
            print("[!!! RED KING ALERT !!!] FIRE DETECTED IN FRAME!")
            
            alarm_thread = threading.Thread(target=play_alarm)
            alarm_thread.start()
            
            last_alarm_time = current_time
    
    # Display the frame
    cv2.imshow("RED KING - Eye of the King", frame)

    # Press ESC to exit
    key = cv2.waitKey(delay) & 0xFF
    if key == 27: 
        break

cap.release()
print("\nVideo ended. Press any key on the image window to close it.")
cv2.waitKey(0) 
cv2.destroyAllWindows()
print("[RED KING] System Shutdown.")
