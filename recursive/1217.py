def power(n, m):
    if m == 1:
        return n
    elif m > 0:
        return n * power(n, m - 1)


for test_case in range(1, 11):
    T = int(input())
    n, m = map(int, input().split())

    result = power(n, m)
    print(f'#{test_case} {result}')
