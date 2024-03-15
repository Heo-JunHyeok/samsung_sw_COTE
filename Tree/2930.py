import sys
import heapq

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = []
    result = []
    for _ in range(n):
        cal = list(map(int, input().split()))
        if cal[0] == 1:
            heapq.heappush(tree, -cal[1])
        else:
            if tree:
                result.append(-heapq.heappop(tree))
            else:
                result.append(-1)

    print(f"#{test_case} {' '.join(list(map(str, result)))}")


# 직접 구현 -> 실패
# def heapify(node):
#     parent = node // 2
#     left = parent * 2
#     right = parent * 2 + 1

#     if parent == 0:
#         return

#     if right < len(tree):
#         if tree[parent] < tree[left] and tree[parent] < tree[right]:
#             if tree[left] <= tree[right]:
#                 tree[parent], tree[right] = tree[right], tree[parent]
#             else:
#                 tree[parent], tree[left] = tree[left], tree[parent]
#             heapify(parent)
#     else:
#         if tree[parent] < tree[node]:
#             tree[parent], tree[node] = tree[node], tree[parent]
#             heapify(parent)


# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     tree = [0]
#     result = []
#     for _ in range(n):
#         cal = list(map(int, input().split()))
#         if cal[0] == 1:
#             tree.append(cal[1])
#             heapify(len(tree) - 1)
#         else:
#             if len(tree) > 1:
#                 tree[1], tree[-1] = tree[-1], tree[1]
#                 result.append(tree.pop())
#                 heapify(len(tree) - 1)
#             else:
#                 result.append(-1)

#     print(f"#{test_case} {' '.join(list(map(str, result)))}")
