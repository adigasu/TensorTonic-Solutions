def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    n = len(values)
    s = sorted(values)

    def percentail(values, pct):
        if pct <= 0:
            return values[0]
        if pct >=100:
            return values[-1]

        k = (n - 1) * pct / 100.0
        f = int(k)
        c = f + 1
        if c >= n:
            return values[f]
        return values[f] + (k - f) * (values[c] - values[f])

    lower = percentail(s, lower_pct)
    upper = percentail(s, upper_pct)

    return [max(lower, min(upper, v)) for v in values]