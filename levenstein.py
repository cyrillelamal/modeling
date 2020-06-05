def levenstein(u: str, v: str) -> int:
    """
    Calculate the Levenshtein distance between u and v.
    """
    n, m = len(u), len(v)

    if m < n:
        u, v = v, u
        n, m = m, n

    cur_row = range(n+1)
    for i in range(1, m+1):
        prev_row, cur_row = cur_row, [i] + [0]*n
        for j in range(1, n+1):
            add, delete, change = prev_row[j] + 1, cur_row[j-1] + 1, prev_row[j - 1]
            if u[j-1] != v[i-1]:
                change += 1
            cur_row[j] = min(add, delete, change)

    return cur_row[n]
