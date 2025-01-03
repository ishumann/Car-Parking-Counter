import cv2

# Open the input video
input_video_path = r'./Image_Video/video.mp4'
cap = cv2.VideoCapture(input_video_path)

# Get the width and height of the frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
output_video_path = './Image_Video/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*"hvc1")  # Codec for .mp4 files
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame (example: convert to grayscale)
    # processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the processed frame to the output video
    out.write(frame)
    # out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
