import cv2
import sys

# Get user-supplied values or use default
if len(sys.argv) > 1:
    imagePath = sys.argv[1]
else:
    imagePath = 'a.jpg'  # Default image path

cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Could not open or find the image at path: {imagePath}")
    sys.exit(1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
