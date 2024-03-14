import sys

sys.stdin = open("input.txt", "r")


def cal_parent(n):
    if n < 0:
        return

    parent = n // 2
    if n % 2:
        tree[parent] = tree[parent * 2] + tree[n]
        cal_parent(n - 2)
    else:
        tree[parent] = tree[n]
        cal_parent(n - 1)


T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)

    for _ in range(m):
        i, v = map(int, input().split())
        tree[i] = v

    cal_parent(n)

    print(f'#{test_case} {tree[l]}')
