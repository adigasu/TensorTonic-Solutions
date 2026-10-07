import math
import numpy as np
def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    if size <= 0:
        print(f"Size={size} must be positive")
        return Null
        
    center = size // 2
    kernel = np.zeros((size, size), dtype=np.float64)
    total = 0
    for r in range(size):
        for c in range(size):
            x = c - center
            y = r - center
            g_x_y = math.exp(-(x**2 + y**2)/ (2 * sigma**2))   
            kernel[r,c] = g_x_y
            total += g_x_y

    return [[weight / total for weight in r] for r in kernel]