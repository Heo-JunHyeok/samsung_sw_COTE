for test_case in range(1, 11):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    count = 0

    # 가로
    for i in range(8):
        for j in range(8 - n + 1):
            row = matrix[i][j : j + n]
            if row == row[::-1]:
                count += 1

    # 세로
    for i in range(8 - n + 1):
        for j in range(8):
            col = []
            for k in range(n):
                col.append(matrix[i + k][j])
            if col == col[::-1]:
                count += 1

    print(f"#{test_case} {count}")
