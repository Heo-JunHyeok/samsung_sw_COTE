T = int(input())

for test_case in range(1, T + 1):
    string = input()

    for i in range(1, len(string) // 2 + 1):
        pattern = string[:i]
        if string[i : i + len(pattern)] == pattern:
            print(f"#{test_case} {len(pattern)}")
            break
    else:
        print(f"#{test_case} 0")
