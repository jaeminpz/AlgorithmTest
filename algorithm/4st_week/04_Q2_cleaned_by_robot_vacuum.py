from collections import deque


current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    #(r,c) 칸의 좌표 , d 바라보는 방향 , d가 0 이면 북, d가 1이면 동, d가 2이면 남, d가 3이면 서
    n = len(room_map)
    m = len(room_map[0])
    count = 0

    while True:
        if room_map[r][c] == 0:
            room_map[r][c] = 2
            count += 1

        cleaned = False
        for _ in range(4):
            d = (d + 3) %4
            nr = r + dr[d]
            nc = c + dc[d]

            if room_map[nr][nc] == 0:
                r, c = nr, nc
                cleaned = True
                break

        if not cleaned:
            back_d = (d + 2) % 4
            br = r + dr[back_d]
            bc = c + dc[back_d]
            옳은
            if room_map[br][bc] == 1:
                break
            else:
                r, c = br, bc


    return count


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))





