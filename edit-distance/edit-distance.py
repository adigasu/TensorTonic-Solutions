def edit_distance(s1: str, s2: str) -> int:
    """
    Find the edit distance between 2 strings s1 & s2
    Returns the minimum number of edits between the strings.
    """
    m = len(s1)
    n = len(s2)

    # Initialize DP table
    dp = [[0] * (n+1) for i in range(m+1)]

    # Initialize s1 and s2 index
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # calculate edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
                