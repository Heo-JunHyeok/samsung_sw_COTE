T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    example = [i * num for i in range(2, 10)]
    num = str(num)
    dict_num = dict()
    for i in num:
        dict_num[i] = num.count(i)
    for drainage in example:
        dict_drainage = dict()
        if len(str(drainage)) == len(str(num)):
            for element in str(drainage):
                dict_drainage[element] = str(drainage).count(element)
            if dict_num == dict_drainage:
                print(f"#{test_case} possible")
                break
    else:
        print(f"#{test_case} impossible")

# 숫자가 같은 배수
# 주어진 num를 재배열하여 num의 배수를 만들 수 있는가
# dict보단 배수를 정렬하여 같은지 확인하는게 더 코드가 깨끗할 것이라 반성한다.
