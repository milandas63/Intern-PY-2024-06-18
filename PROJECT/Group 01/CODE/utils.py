from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def calculate_metrics(detected_faces, ground_truth_faces):
    # Convert rectangles to binary labels
    y_true = [1] * len(ground_truth_faces) + [0] * (len(detected_faces) - len(ground_truth_faces))
    y_pred = [1 if face in detected_faces else 0 for face in ground_truth_faces]
    
    # Handle empty cases
    if not y_true or not y_pred:
        return 0.0, 0.0, 0.0
    
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    return precision, recall, f1

def analyze_results(detected_faces, ground_truth_faces, f1):
    precision, recall, _ = calculate_metrics(detected_faces, ground_truth_faces)
    
    print(f"Detected faces: {detected_faces}")
    print(f"Ground truth faces: {ground_truth_faces}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")
