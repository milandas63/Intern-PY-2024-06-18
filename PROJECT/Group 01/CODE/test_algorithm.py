from face_detection import detect_faces

# Function to test the algorithm on multiple images
def test_algorithm(image_paths, resize_factor=0.5):
    results = []
    for path in image_paths:
        faces, image = detect_faces(path, resize_factor)
        results.append((path, faces))
        print(f"Image: {path}, Faces detected: {len(faces)}")
    return results

if __name__ == "__main__":
    # Sample image paths for testing
    image_paths = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']
    test_results = test_algorithm(image_paths)

