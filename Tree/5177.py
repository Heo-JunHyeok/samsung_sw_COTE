import sys

sys.stdin = open("input.txt", "r")


def heapify(node):
    parent = node // 2

    if parent == 0:
        return

    if tree[parent] > tree[node]:
        tree[parent], tree[node] = tree[node], tree[parent]
        heapify(parent)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0]

    for i in map(int, input().split()):
        tree.append(i)
        heapify(len(tree) - 1)

    result = 0
    while n != 1:
        result += tree[n // 2]
        n //= 2

    print(f"#{test_case} {result}")
