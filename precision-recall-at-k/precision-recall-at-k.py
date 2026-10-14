def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k = recommended[:k]
    hits = sum(i in relevant for i in top_k)
    precision_k = hits/k
    recall_k = hits / len(relevant)
    return [precision_k, recall_k]