def evaluate(detected_faces, ground_truth_faces):
    # Create lists to hold the results
    y_true = []
    y_pred = []

    # Compare detected faces with ground truth faces
    for gt_face in ground_truth_faces:
        match_found = False
        for detected_face in detected_faces:
            # Simple overlap check
            if (gt_face.left() <= detected_face.right() and gt_face.right() >= detected_face.left() and
                gt_face.top() <= detected_face.bottom() and gt_face.bottom() >= detected_face.top()):
                match_found = True
                break
        y_true.append(1)  # ground truth face
        y_pred.append(1 if match_found else 0)  # detected face

    # Calculate precision, recall, and F1-score manually
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1
