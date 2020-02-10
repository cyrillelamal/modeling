A = [
    [5, 7, 6, 5],
    [7, 10, 8, 7],
    [6, 8, 10, 9],
    [5, 7, 9, 10],
]

B = [23, 32, 33, 31]


def gaussian_elimination(a: list, b: list) -> list:
    """Return X-vector resulting from Gaussian Elimination method"""
    a = [ai + [bi] for ai, bi in zip(a, b)]  # Concatenated matrix
    
    # Direct
    for i in range(len(a) - 1):
        aii = a[i][i]  # Must be the same for all next iterations!

        # ai_ row
        for j in range(len(a[i])):
            a[i][j] /= aii

        # Next rows
        for k in range(i + 1, len(a)):
            aki = a[k][i]  # Must be the same for all next iterations!

            for j in range(i, len(a[i])):
                a[k][j] = a[k][j] - a[i][j] * aki

    # Reverse
    # n - number of columns (xn in row) (n|n+1)
    n = len(a[0]) - 1

    n -= 1  # Indexes conversion

    x = [0.0] * (n + 1)

    x[n] = (a[n][n+1] / a[n][n])

    for i in range(n - 1, -1, -1):
        x[i] = a[i][n+1] - sum([a[i][j] * x[j] for j in range(i + 1, n + 1)])

    return x


if __name__ == '__main__':
    print(gaussian_elimination(A, B))
