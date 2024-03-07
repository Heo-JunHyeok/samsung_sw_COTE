def sub_cnt(index, sum_num, numbers):
    # 기저 사례
    if sum_num == k:
        return 1
    if sum_num > k or index < 0:
        return 0

    # 해당 인덱스의 값을 더한 경우와 더하지 않은 경우
    cnt = sub_cnt(index - 1, sum_num, numbers) + sub_cnt(
        index - 1, sum_num + numbers[index], numbers
    )
    return cnt


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    result = sub_cnt(n - 1, 0, numbers)

    print(f'#{test_case} {result}')
