import sys
sys.stdin = open("brick_input.txt", "r")
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 특정 위치의 벽돌을 1회 부수는 함수
def break_brick(x, y, value, board):
    #
    queue = deque([x, y, value])

    while queue:
        cur_x, cur_y, val = queue.popleft()
        board[cur_x][cur_y] = 0

        for dist in range(1, val):
            for i in range(4):
                now_x = cur_x + dist * dx[i]
                now_y = cur_y + dist * dy[i]

                if 0 <= now_x < H and 0 <= now_y < W and board[now_x][now_y] != 0:
                    queue.append((now_x, now_y, board[now_x][now_y]))

    # # 해당 벽돌의 값이 1일 때
    # if value <= 1:
    #     board[x][y] = 0
    # # 그 외의 숫자
    # else:
    #     # 그 길이에 대한 재귀함수
    #     # 폭발 범위 내의 수를 하나씩
    #     for num in range(1, value):
    #         # 4 방위 확인
    #         for idx in range(4):
    #             # 각 x,y 해당 인덱스 위치
    #             now_x = x + (value-1) * dx[idx]
    #             now_y = y + (value-1) * dy[idx]
    #             # 해당 위치가 board 내부에 있으며 그 값이 0이 아닌 경우
    #             if 0 <= now_x < W and 0 <= now_y < H and board[now_x][now_y] != 0:
    #                 break_brick(now_x, now_y, board[now_x][now_y], board)

# 벽돌은 아래로 내리는 함수
def drop_brick(W, H, board):
    # 세로에 있는 숫자를 정렬하는 리스트(행과 열이 반전되어있음)
    row_list = []
    for col in range(W):
        # 이번 열의 숫자를 담는 리스트
        height_nums = []
        for row in range(H):
            # 해당 위치의 값이 0이 아니라면 리스트에 추가
            if board[row][col] != 0:
                height_nums.append(board[row][col])
        row_list.append(height_nums)

    # 보드 초기화
    for i in range(H):
        for j in range(W):
            board[i][j] = 0

    # 찾은 숫자를 아래로 재배치
    for col in range(len(row_list)):
        # 이번 높이
        length = len(row_list[col])
        # 아래에서부터 채우기
        for row in range(length-1, -1, -1):
            board[H - (length - row)][col] = row_list[col][row]


# 시간의 순서에 따른 행동 가능한 경우의 수가 dfs임
def dfs(board, trial):
    # 벽돌 수가 최소일 때 visited
    total_sum = float(-'inf')
    # 방문한
    visited = []

    #
    while True:
        # 부술 수 있는 맨위 벽돌 위치, 값 모음
        tops = []
        # 가로 세로 길이동안
        for col in range(W):
            for row in range(H):
                # 제일 먼저 찾은 0이 아닌 값을
                if board[row][col] != 0:
                    # 위치와 함께 tops에 저장
                    tops.append([row, col, board[row][col]])
                    break

        # 맨 위에서 들어갈 수 있는 방법
        for top in tops:
            stack = [top]
            # visited = False 가 아닐 경우
            while stack:
                node = stack.pop()











T = int(input())

for test_case in range(1, T + 1):
    # N : 떨어트릴 벽돌의 개수
    # W : 가로의 길이
    # H : 세로의 길이
    N, W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]

    visited = [[0] * W for _ in range(H)]

    # 현재 부술 수 있는 벽돌의 집합
    tops = []
    for i in range(W):
        for j in range(H):
            if board[i][j] != 0:
                tops.append([i, j, board[i][j]])

    dfs(board, 4)

