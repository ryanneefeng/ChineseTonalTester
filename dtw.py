def build_cost_matrix(sequence_a, sequence_b):
    n = len(sequence_a)
    m = len(sequence_b)
    cost_matrix = []
    for i in range(n + 1):
        row = []
        for j in range(m + 1):
            row.append(float("inf"))
        cost_matrix.append(row)
    cost_matrix[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            point_cost = abs(sequence_a[i - 1] - sequence_b[j - 1])
            best_previous = min(cost_matrix[i - 1][j], cost_matrix[i][j - 1], cost_matrix[i - 1][j - 1])
            cost_matrix[i][j] = point_cost + best_previous
    return cost_matrix

def backtrack_path(cost_matrix):
    i = len(cost_matrix) - 1
    j = len(cost_matrix[0]) - 1
    path = [(i, j)]
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            diagonal = cost_matrix[i - 1][j - 1]
            up = cost_matrix[i - 1][j]
            left = cost_matrix[i][j - 1]
            best = min(diagonal, up, left)
            if best == diagonal:
                i -= 1
                j -= 1
            elif best == up:
                i -= 1
            else:
                j -= 1
        path.append((i, j))
    path.reverse()
    return path

def align(sequence_a, sequence_b):
    cost_matrix = build_cost_matrix(sequence_a, sequence_b)
    path = backtrack_path(cost_matrix)
    total_cost = cost_matrix[len(sequence_a)][len(sequence_b)]
    return path, total_cost