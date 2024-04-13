def check_range(diff, low, high):
    return True if (low <= diff and diff <= high) else False

def get_splites(egg_plate: list, low, high):
    splites = list()
    line_number = len(egg_plate)
    
    for row in range(line_number):
        if row == line_number-1 :
            break
        for col in range(line_number):
            if col == line_number-1 :
                break
            
            # 오른쪽 확인
            diff = abs(egg_plate[row][col] - egg_plate[row][col+1])
            if check_range(diff, low, high):
                splites.append([(row,col), (row,col+1)])
            # 아래쪽 확인
            diff = abs(egg_plate[row][col] - egg_plate[row+1][col])
            if check_range(diff, low, high):
                splites.append([(row,col), (row+1,col)])
    return splites            

        
def merge_splites(splites):
    merged_splites = {}
    on_depend = set()

    for p1, p2 in splites:
        # print(f"p1 {p1}, p2 {p2}")
        keys = merged_splites.keys()
        if p1 in keys and p2 in keys:

            p1_key = merged_splites[p1]
            p2_key = merged_splites[p2]

            # 두개 합치기
            merged_splites[p1_key] += merged_splites[p2_key][:]

            # 키 교체
            on_depend.add(*merged_splites[p2_key])
            merged_splites[p2_key] = merged_splites[p1_key]

        elif p1 in keys:
            merged_splites[p2] = merged_splites[p1]
            merged_splites[p1].append(p2)
            on_depend.add(p2)


        elif p2 in keys:
            merged_splites[p1] = merged_splites[p2]
            merged_splites[p2].append(p1)
            on_depend.add(p1)


        else:
            # 키 생성
            merged_splites[p1] = [p1, p2]
            merged_splites[p2] = merged_splites[p1]
            on_depend.add(p2)
    
    result = []

    # print(f"merged splites {merged_splites}")
    for key, points in merged_splites.items():
        if not key in on_depend:
            result.append(points)
            # print(f" points {points}, result {result}")

    return result


n, L, R = map(int, input().split())


egg_plate = []

for row in range(n):
    egg_plate.append(list(map(int, input().split())))

count = 0
while True:
    # 이동할 게 있는지 확인 
    splites = get_splites(egg_plate,L,R)
    if not splites : 
        break

    # 계란틀의 선을 분리
    merged_splites = merge_splites(splites)
    # print(merged_splites)
    # 계란을 합치고, 다시 분리
    for splites in merged_splites :
        egg_sum = 0
        for row, col in splites :
            egg_sum += egg_plate[row][col]
        egg_average = egg_sum // len(splites)
        for row, col in splites :
            egg_plate[row][col] = egg_average


    count += 1


print(count)