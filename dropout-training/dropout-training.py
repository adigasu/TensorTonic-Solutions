import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Apply dropout to input with prob. p
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    if p >= 1.0 or p < 0:
        print(f'Dropout probability p={p} should be within [0,1)')
        return None

    x = np.asarray(x, float)
    
    rng = rng if isinstance(rng, np.random.Generator) else np.random.default_rng(0)
    
    dropout_pattern = rng.random(x.shape)
    mul = 1.0 / (1 - p)
    mask = (dropout_pattern < (1-p)) * mul
    x = x * mask
    return x, mask
    

    