import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Label smoothing loss: compute cross-entropy loss for the smoothed target distribution.
    """
    loss = 0.0
    K = len(predictions)
    if K <= 0:
        print("Number of class greater than 1")
        return 0

    if target > K or target < 0:
        print(f"Target class={target} should be within 0 to {K}")
        return 0
        
    for i, p in enumerate(predictions):
        if i == target:
            q = (1 -  epsilon) + epsilon/K
        else:
            q = epsilon/K
        loss += - q * math.log(p)

    return loss
        