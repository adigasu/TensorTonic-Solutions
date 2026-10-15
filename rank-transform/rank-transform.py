def rank_transform(values: list) -> list:
    """
    Returns the one-based average rank of every value.
    """
    n = len(values)
    s_idx = sorted(range(n), key=lambda i: values[i])
    ranks = [0.0] * n

    i = 0
    while i < n:
        j = i + 1
        while j < n and values[s_idx[i]] == values[s_idx[j]]:
            j += 1
        if j - i > 1:
            average_rank = sum(range(i+1, j+1)) / (j - i)
            for r in range(i, j):
                ranks[s_idx[r]] = average_rank
        else:
            ranks[s_idx[i]] = i + 1
        i = j
        
    return ranks

    