import dlib
from face_detection import detect_faces
from evaluation import evaluate
from analyze_results import analyze_results
from alternative_detection import detect_faces_haar
from draw_boxes import draw_bounding_boxes
from display_results import display_image_with_boxes



# from utils import analyze_results, calculate_metrics

# # Example face detection results
# detected_faces = ['face1', 'face2', 'face3']
# ground_truth_faces = ['face2', 'face3', 'face4']

# # Calculate metrics
# precision, recall, f1_score = calculate_metrics(detected_faces, ground_truth_faces)

# # Analyze results
# analyze_results(detected_faces, ground_truth_faces, f1_score)




import cv2
import numpy as np
from utils import analyze_results, calculate_metrics


# Example face detection results using numpy and OpenCV
detected_faces = [cv2.rectangle(np.zeros((100, 100, 3), dtype=np.uint8), (10, 10), (20, 20), (255, 0, 0), 2)]
ground_truth_faces = [cv2.rectangle(np.zeros((100, 100, 3), dtype=np.uint8), (15, 15), (25, 25), (0, 255, 0), 2)]

# For simplicity in calculation, use string identifiers
detected_faces_labels = ['face1', 'face2', 'face3']
ground_truth_faces_labels = ['face2', 'face3', 'face4']

# Calculate metrics
precision, recall, f1_score = calculate_metrics(detected_faces_labels, ground_truth_faces_labels)

# Analyze results
analyze_results(detected_faces_labels, ground_truth_faces_labels, f1_score)

# Function to display image with bounding boxes
def display_image_with_boxes(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("Image with Boxes", image_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example image for display
image_with_boxes = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.rectangle(image_with_boxes, (50, 50), (150, 150), (255, 0, 0), 2)
cv2.rectangle(image_with_boxes, (200, 200), (300, 300), (0, 255, 0), 2)

try:
    display_image_with_boxes(image_with_boxes)
except MemoryError as e:
    print(f"MemoryError: {e}")





# Example ground truth faces (these would normally come from your dataset annotations)
ground_truth_faces = [dlib.rectangle(50, 50, 150, 150), dlib.rectangle(200, 200, 300, 300)]

if __name__ == "__main__":
    sample_image_path = 'images/sample_image.jpg'
    
    # Evaluate using dlib detector
    detected_faces, image_with_faces = detect_faces(sample_image_path)
    precision, recall, f1 = evaluate(detected_faces, ground_truth_faces)
    print(f"Evaluation with dlib detector - Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1:.2f}")
    
    # Analyze results
    analyze_results(detected_faces, ground_truth_faces, f1)
    
    # Parameter tuning and re-evaluation
    for upsample_num_times in [1, 2]:
        for threshold in [0, 1]:
            try:
                detected_faces_params, _ = detect_faces(sample_image_path, upsample_num_times)
                precision_params, recall_params, f1_params = evaluate(detected_faces_params, ground_truth_faces)
                print(f"Upsample: {upsample_num_times}, Threshold: {threshold}, Precision: {precision_params:.2f}, Recall: {recall_params:.2f}, F1-score: {f1_params:.2f}")
            except Exception as e:
                print(f"Error in detect_faces: {e}")
    
    # Explore alternatives using Haar cascades
    try:
        detected_faces_haar = detect_faces_haar(sample_image_path)
        precision_haar, recall_haar, f1_haar = evaluate(detected_faces_haar, ground_truth_faces)
        print(f"Haar Cascades - Precision: {precision_haar:.2f}, Recall: {recall_haar:.2f}, F1-score: {f1_haar:.2f}")
    except Exception as e:
        print(f"Error in detect_faces_haar: {e}")

    # Draw bounding boxes and display results
    image_with_boxes = draw_bounding_boxes(image_with_faces, detected_faces)
    display_image_with_boxes(image_with_boxes)
