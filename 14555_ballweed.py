T = int(input())

for test_case in range(1, T + 1):
    line = input()
    if "()" or "(|" or "|)" in line:
        ball: int = line.count("()") + line.count("(|") + line.count("|)")

    print(f"#{test_case} {ball}")


# 수풀(|)에 가려진 공을 포함하여 최소 몇개의 공이 존재하는지 판별
