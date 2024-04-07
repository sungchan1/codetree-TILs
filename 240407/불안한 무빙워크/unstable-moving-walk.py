n, k = map(int, input().split())
panel_safety = list(map(int, input().split()))
stand_positions = [False] * (2*n)

count = 1
start_index = 0
while True:
    # 무빙워크 한칸 회전
    start_index = start_index-1 if start_index >0 else 2*n-1
    end_index = start_index+n-1
    end_index_round = end_index % (2*n)
    # print(start_index, end_index)

    for position in range(end_index, start_index-1, -1):
        position = position % (2*n)

        # 사람 없으면 다음으로
        if not stand_positions[position] : 
            continue

        if position == end_index_round:
            stand_positions[position] = False
            continue
        # 사람 다음 칸 이동
        next_position = (position+1) % (2*n)
        if panel_safety[next_position] >0 and not stand_positions[next_position]:
            # print("다음 칸 이동", next_position, end_index)
            stand_positions[position] = False
            stand_positions[next_position] = True
            panel_safety[next_position] -= 1
            # 끝 칸이면 나가

            if next_position == end_index_round:
                stand_positions[next_position] = False

    # 1번칸에 사람 없고, 안정성 0이 아니면 한명 올림
    if panel_safety[start_index] >0 and not stand_positions[start_index]:
        stand_positions[start_index] = True
        panel_safety[start_index] -= 1

    # # 안정성이 0인 칸이 k개 이상이면 종료
    if panel_safety.count(0) >= k:
        break
    # print(count, start_index+1, end_index+1, stand_positions)
    count += 1

print(count)