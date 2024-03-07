T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [input().split() for _ in range(n)]
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == "1":
                cnt += 1
            if puzzle[i][j] == "0" or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

        cnt = 0
        for j in range(n):
            if puzzle[j][i] == "1":
                cnt += 1
            if puzzle[j][i] == "0" or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f"#{test_case} {result}")
