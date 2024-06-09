def count_minimum_edit_distance(word1, word2):
    """
    Count the minimum edit distance between two words
    :param word1:
    :param word2:
    :return:
    """
    # Create a matrix of size (m+1)*(n+1) where m is the length of word1 and n is the length of word2
    m = len(word1)
    n = len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and the first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


if __name__ == "__main__":
    print(count_minimum_edit_distance("hi", "yu"))
