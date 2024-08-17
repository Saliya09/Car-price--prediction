import cv2
import torch
import numpy as np
from sort import Sort

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Initialize video capture
cap = cv2.VideoCapture("video/people.mp4")

# Initialize the SORT tracker
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# Store counts of people
total_count = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()

    # Filter detections for 'person' class
    person_detections = [d for d in detections if int(d[5]) == 0]  # YOLOv5 class index for 'person' is 0

    # Prepare detections for SORT (only consider necessary fields)
    detections_for_sort = np.array([[x1, y1, x2, y2, conf] for x1, y1, x2, y2, conf, cls in person_detections])

    # Update tracker with the detections
    tracked_objects = tracker.update(detections_for_sort)

    # Draw bounding boxes and IDs on the frame
    for obj in tracked_objects:
        x1, y1, x2, y2, obj_id = [int(coord) for coord in obj]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {int(obj_id)}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Count unique IDs to avoid recounting
        if obj_id not in total_count:
            total_count.append(obj_id)

    # Display the total people count
    cv2.putText(frame, f'People Count: {len(total_count)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Advanced Crowd Counting', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
