T = 10
for test_case in range(1, T + 1):
    building_num = int(input())
    building_height = list(map(int, input().split()))
    result = 0

    if building_num == 4:
        max_building = max_building(building_height)
        second = sorted(building_height[i - 2 : i + 3], reverse=True)
        result = max_building = second[1]
    else:
        for i in range(2, building_num - 2):
            max_building = max(building_height[i - 2 : i + 3])
            second = sorted(building_height[i - 2 : i + 3], reverse=True)
            if building_height[i] == max_building:
                print(building_height[i - 2 : i + 3], max_building, second)
                result += max_building - second[1]
        print(f"#{test_case} {result}")

# 예외처리가 부족해보임
# 일단 풀었음
