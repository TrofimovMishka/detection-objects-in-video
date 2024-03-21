import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Check if frame is captured successfully
if not ret:
    print("Error capturing frame")
    cap.release()
    exit()

# Define filename for the image
filename = "captured_image.jpg"

# Save the frame as an image
cv2.imwrite(filename, frame)

# Print success message
print(f"Image saved successfully as {filename}")

# Release the camera
cap.release()

# Close all open windows (if any)
cv2.destroyAllWindows()
