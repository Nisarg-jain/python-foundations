"""
Machine Learning workflow prototype:
Demonstrating feature separation, train-test splitting, and evaluation metrics from scratch.
"""

def split_train_test(
    features: list[list[float]], 
    labels: list[int], 
    test_ratio: float = 0.2
) -> tuple[list[list[float]], list[list[float]], list[int], list[int]]:
    """Splits features and labels into training and testing sets deterministically."""
    if len(features) != len(labels):
        raise ValueError("Features and labels must have the same number of samples.")

    split_index = int(len(features) * (1 - test_ratio))
    
    x_train, x_test = features[:split_index], features[split_index:]
    y_train, y_test = labels[:split_index], labels[split_index:]
    
    return x_train, x_test, y_train, y_test


def calculate_metrics(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    """Computes basic binary classification performance metrics."""
    if len(y_true) != len(y_pred):
        raise ValueError("True labels and predicted labels must match in length.")

    true_positive = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    true_negative = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)
    false_positive = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    false_negative = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)

    total_samples = len(y_true)
    accuracy = (true_positive + true_negative) / total_samples if total_samples else 0.0
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0.0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0.0

    return {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4)
    }


if __name__ == "__main__":
    # Synthetic dataset: [Age, Income_Index] -> Subscribed (1/0)
    raw_features = [
        [22, 1.5], [25, 2.0], [47, 5.2], [52, 6.1],
        [46, 4.8], [56, 7.0], [23, 1.2], [40, 3.8],
        [60, 8.2], [21, 1.0]
    ]
    raw_labels = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]

    # 1. Dataset Partitioning
    x_train, x_test, y_train, y_test = split_train_test(raw_features, raw_labels, test_ratio=0.3)
    print(f"Training samples: {len(x_train)} | Testing samples: {len(x_test)}")

    # 2. Simulated Model Predictions on Test Partition
    si