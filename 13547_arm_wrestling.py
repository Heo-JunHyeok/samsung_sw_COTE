T = int(input())

for test_case in range(1, T + 1):
    test = input()
    if test.count("x") > 7:
        print(f"#{test_case} NO")
    else:
        print(f"#{test_case} YES")

# 팔씨름을 이길 가능성이 있는가
# 7번까지 져도 됨.
