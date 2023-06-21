T = int(input())

for test_case in range(1, T + 1):
    test = list(input())
    min_test, max_test = "".join(test), "".join(test)
    if "".join(test) == "0":
        print(f"#{test_case} 0 0")
    else:
        for i in range(len(test) - 1):
            for j in range(i + 1, len(test)):
                if test[i] != test[j]:
                    test[i], test[j] = test[j], test[i]
                    if test[0] == "0":
                        test[i], test[j] = test[j], test[i]
                        continue
                    else:
                        min_test = min(min_test, "".join(test))
                        max_test = max(max_test, "".join(test))
                        test[i], test[j] = test[j], test[i]
        print(f"#{test_case} {min_test} {max_test}")


# 한번만 이동해서 최소값, 최대값 구하기
# continue: 다음 loop로 넘어가기
# break loop 벗어나기
