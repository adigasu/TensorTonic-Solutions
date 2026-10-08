def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    out = []
    w_len = len(weights)
    w_sum = sum(weights)

    for i in range(len(values) - w_len + 1):
        total = sum(v * w for v, w in zip(values[i : i + w_len], weights))
        out.append(total / w_sum)

    return out