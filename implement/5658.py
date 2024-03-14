import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())

    queue = deque(input())
    password = []

    line = n // 4
    for _ in range(n):
        numbers = list(queue)
        for i in range(0, n, line):
            password.append(int("".join(numbers[i : i + line]), 16))
        queue.rotate(1)

    password = sorted(list(set(password)), reverse=True)

    print(f'#{test_case} {password[k - 1]}')
