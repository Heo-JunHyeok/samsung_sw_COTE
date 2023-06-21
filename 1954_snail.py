T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    arr = [[0 for j in range(n)] for i in range(n)]
    num, row, col, direction = 1, 0, -1, 1

    while n > 0:
        for _ in range(n):
            col += direction
            arr[row][col] = num
            num += 1
        n -= 1
        for _ in range(n):
            row += direction
            arr[row][col] = num
            num += 1
        direction *= -1

    for i in arr:
        for j in i:
            print(j, end=" ")
        print(end="\n")

# 달팽이 배열
# 못품
