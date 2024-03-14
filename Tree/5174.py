import sys

sys.stdin = open("input.txt", "r")


def preorder(n):
    global result
    if n:
        result += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int, sys.stdin.readline().split())
    inputlist = list(map(int, sys.stdin.readline().split()))

    result = 0

    # 노드 개수 e+1, 0 인덱스 안 씀
    ch1 = [0] * (e + 2)
    ch2 = [0] * (e + 2)

    # 저장
    for i in range(0, len(inputlist), 2):
        parent, child = inputlist[i], inputlist[i + 1]

        if ch1[parent] == 0:
            ch1[parent] = child
        else:
            ch2[parent] = child

    # 순회
    preorder(n)

    print(f"#{test_case} {result}")
