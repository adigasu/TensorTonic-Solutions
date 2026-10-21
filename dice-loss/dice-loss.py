import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    compute dice loss (float)
    """
    n = len(p)
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(p) != len(y):
        print(f"lenght of pred p and target y are not same")
        return -1
    overlap = np.sum(p * y)
    dice = (2.0 * overlap + eps) / (np.sum(p) + np.sum(y) + eps)
    return float(1.0 - dice)