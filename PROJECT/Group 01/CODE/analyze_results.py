# Analyze the evaluation metrics and print suggestions for improvement
def analyze_results(precision, recall, f1):
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")
    
    if precision < 0.8:
        print("Consider reducing false positives by adjusting the detection threshold.")
    
    if recall < 0.8:
        print("Consider increasing the sensitivity of the face detector to reduce false negatives.")
    
    if f1 < 0.8:
        print("Overall performance can be improved by balancing precision and recall.")
    
    # Additional specific analysis based on data
    print("Analyze missed detections and false positives for specific patterns or cases.")
