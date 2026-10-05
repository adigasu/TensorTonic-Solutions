def promote_model(models: list) -> str:
    """
    Returns the model name as a string.
    """
    if len(models) == 0:
        return None
    if len(models) == 1:
        return models[0]["name"]
    best_model = models[0]

    for m in models[1:]:
        if m["accuracy"] > best_model["accuracy"]:
            best_model = m
        elif m["accuracy"] == best_model["accuracy"]:
            if m["latency"] < best_model["latency"]:
                best_model = m
            elif m["latency"] == best_model["latency"]:
                if m["timestamp"] > best_model["timestamp"]:
                    best_model = m
    return best_model["name"]