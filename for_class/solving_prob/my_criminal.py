import sys
sys.stdin = open("criminal_input.txt", "r")
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 상하좌우 순서, 이어져 있는 순서
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}

def bfs(start_y, start_x):
    dq = deque([(start_y, start_x)])
    visited[start_y][start_x] = 1

    while dq:
        cur_y, cur_x = dq.popleft()
        dirs = types[sewer[start_y][start_x]]

        for i in range(4):
            if dirs[i] == 0:
                continue

            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            # 안되는 경우 제외
            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= M:
                continue

            # 이미 방문한 경우
            if visited[next_y][next_x]:
                continue

            # 다음 좌표가 갈 수 없는 곳인 경우
            if sewer[next_y][next_x] == 0:
                continue

            # 앞선 상황들을 전부 해결하면
            next_dirs = types[sewer[next_y][next_x]]

            # 그 후의 상황
            # 현재 상좌 -> 다음 하우 안뚫렸으면 못감
            if i % 2 == 0 and next_dirs[i + 1] == 0:
                continue

            # 현재 하우   -> next_dirs가 상좌 안뚫렸으면 못감
            if i % 2 == 1 and next_dirs[i - 1] == 0:
                continue

            # L 시간이 넘어가면 볼 필요 없다
            if visited[cur_y][cur_x] + 1 > L:
                continue

            visited[next_y][next_x] += 1
            dq.append((next_y, next_x))



T = int(input())

for test_case in range(1, T + 1):
    # N : 세로의 길이
    # M : 가로의 길이
    # R : 맨홀 뚜껑 세로 위치
    # C : 맨홀 뚜껑 가로 위치
    # L : 탈출 후 소요 시간
    N, M, R, C, L = map(int, input().split())

    sewer = [list(map(int, input().split())) for _ in range(N)]

    # 방문 지점 확인
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    # visited에서 L 시간 이하로 방문한모든 곳을 count
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f"{test_case} {cnt}")
