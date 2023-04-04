
import cv2
import face_recognition

# Load the image
img_path = "/path-to-image/image.jpg"
image = cv2.imread(img_path)
# image = cv2.imread('image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_recognition.face_locations(gray)

# Draw rectangles around the detected faces
for face in faces:
    top, right, bottom, left = face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the image with the detected faces
cv2.imshow('Faces found', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the image data
print(image)

