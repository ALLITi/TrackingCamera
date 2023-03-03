import cv2
import os

# Define input videos
input_videos = [
    r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\videos\001.avi',
    r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\videos\002.avi',
    r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\videos\003.avi',
    r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\videos\004.avi',
    r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\videos\005.avi'
]

# Define output video properties
fps = 30
width = 640
height = 480

# Create output video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(r'C:\Users\genus\PycharmProjects\Yolo7Tracking\yolov7\merged.avi', fourcc, fps, (width, height))

# Loop through input videos and add frames to output video
for input_video in input_videos:
    # Open input video
    cap = cv2.VideoCapture(input_video)

    # Loop through frames and add them to output video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        output_video.write(frame)

    # Release input video
    cap.release()

# Release output video
output_video.release()

print('Merged video saved to merged.avi')
