import sys

sys.stdin = open("input.txt", "r")


def inorder(a):
    global result
    if a <= n:
        inorder(a * 2)
        nodelist[a] = result
        result += 1
        inorder(a * 2 + 1)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nodelist = [0] * (n + 1)
    result = 1

    inorder(1)

    print(f'#{test_case} {nodelist[1]} {nodelist[n//2]}')
