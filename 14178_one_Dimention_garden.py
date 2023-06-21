import math

T = int(input())

for test_case in range(1, T + 1):
    n, d = map(int, input().split())
    unit = 2 * d + 1
    print(f"#{test_case} {math.ceil(n/unit)}")


# x좌표 기준으로 [x-d,x+d]에 물이 뿌려짐.
# 모든 정원에 물을 뿌릴 수 있는 최소값
