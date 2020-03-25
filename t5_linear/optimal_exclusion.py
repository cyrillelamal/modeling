def optimal_exclusion(a: list, b: list) -> list:
    """Return X-vector resulting from Gaussian Optimal Elimination method"""
    # all the difference: not unary elements on the main diagonal
    a = [ai + [bi] for ai, bi in zip(a, b)]  # Concatenated matrix

    # direct
    for i in range(len(a) - 1):
        aii = a[i][i]

        # !!! ======= !!!
        #   no ai_ row
        # !!! ======= !!!

        for k in range(i + 1, len(a)):
            aki = a[k][i] / aii

            for j in range(i, len(a[i])):
                a[k][j] = a[k][j] - a[i][j] * aki

    # reverse
    # n - number of columns (xn in row) (n|n+1)
    n = len(a[0]) - 1

    n -= 1  # indexes conversion

    x = [0.0] * (n + 1)
    x[n] = (a[n][n + 1] / a[n][n])
    for i in range(n - 1, -1, -1):
        x[i] = (a[i][n+1] - sum([a[i][j] * x[j] for j in range(i + 1, n + 1)])) / a[i][i]

    return x


if __name__ == '__main__':
    A = [
        [5, 7, 6, 5],
        [7, 10, 8, 7],
        [6, 8, 10, 9],
        [5, 7, 9, 10],
    ]

    B = [23, 32, 33, 31]

    print(optimal_exclusion(A, B))
