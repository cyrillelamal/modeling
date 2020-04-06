# i = i..(n-1)
# k = 1..n, k != i
# j = i..(n+1)
# a[k][k]_ = a[k][k] - (a[k][i])/(a[i][i]) * a[i][j] =  a[k][j] - a[k][i]_*a[i][j]


def gauss_jordan(a: list, b: list) -> list:
    # Concatenated matrix
    a = [ai + [bi] for ai, bi in zip(a, b)]

    n = len(a)

    for i in range(n):
        for j in range(i+1, n+1):
            a[i][j] = a[i][j] / a[i][i]
        a[i][i] = 1

        for k in range(n):
            if k != i:
                kp = a[k][i]
                for j in range(i+1, n+1):
                    a[k][j] = a[k][j] - a[i][j] * kp
            a[k][i] = 0

    x = [a[i][n] for i in range(n)]

    return x


if __name__ == '__main__':
    A = [
        [5, 7, 6, 5],
        [7, 10, 8, 7],
        [6, 8, 10, 9],
        [5, 7, 9, 10],
    ]

    B = [23, 32, 33, 31]

    print(gauss_jordan(A, B))
