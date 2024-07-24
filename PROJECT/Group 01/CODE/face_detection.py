import cv2
import dlib

# Initialize dlib's face detector
detector = dlib.get_frontal_face_detector()

def detect_faces(image_path, upsample_num_times=1):
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize image if it's too large
    max_size = 800
    height, width = image.shape[:2]
    if max(height, width) > max_size:
        scaling_factor = max_size / float(max(height, width))
        image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = detector(gray, upsample_num_times)
    
    return faces, image
