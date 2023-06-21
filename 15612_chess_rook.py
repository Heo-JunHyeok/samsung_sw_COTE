T = int(input())

for test_case in range(1, T + 1):
    check = {i: False for i in range(8)}
    board = []
    for i in range(8):
        board.append(input())

    for line in board:
        if line.count("0") == 1:
            if not check[line.find("0")]:
                check[line.find("0")] = True
            else:
                print(f"#{test_case} no")
                break
        else:
            print(f"#{test_case} no")
            break
    else:
        print(f"#{test_case} yes")

# 체스판 위에 8개의 룩이 존재하고 룩이 모두 간섭할 수 없는 위치인지 판별
