import os
import cv2

# Define the image path
image_path = 'a.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: The file does not exist at the specified path.")
else:
    print("File exists.")

    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not open or find the image.")
    else:
        print("Image loaded successfully.")
        
        # Get original dimensions
        original_height, original_width = image.shape[:2]
        print(f"Original dimensions: {original_width}x{original_height}")

        # Define the new size (e.g., width=800, height proportional)
        new_width = 800
        aspect_ratio = new_width / float(original_width)
        new_height = int(original_height * aspect_ratio)

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height))
        print(f"Resized dimensions: {new_width}x{new_height}")

        # Display the resized image
        cv2.imshow('Resized Image', resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Print the current working directory
print("Current working directory:", os.getcwd())
