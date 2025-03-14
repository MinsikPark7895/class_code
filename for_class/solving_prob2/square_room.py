import sys
sys.stdin = open("square_input.txt", "r")

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# # 보드 현재 위치에서 주변 4방위 확인
# def check_surrounding(x, y, board):
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         # 주위 델타가 보드 내부에 있을 때
#         if 0 <= new_x < len(board[y]) and 0 <= new_y < len(board):
#             # 주변 4 방위 중 1만큼 큰 값이 있는 확인
#             if board[y][x] + 1 == board[new_y][new_x]:
#                 return 1
#     return 0

T = int(input())

for test_case in range(1, T + 1):
    # 보드 가로세로 길이
    N = int(input())
    # 보드 받기
    board = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 리스트 표시
    visited = [0] * (N * N + 1)

    for y in range(N):
        for x in range(N):
            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]
                if 0 <= new_y < N and 0 <= new_x < N:
                    if board[new_y][new_x] == board[y][x] + 1:
                        visited[board[y][x]] = 1
                        break

    max_len = 0
    length = 0
    start = 0

    for i in range(1, N * N + 1):
        if visited[i] == 1:
            length += 1
        else:
            if max_len < length:
                max_len = length
                start = i - length
            length = 0

    print(f"#{test_case} {start} {max_len + 1}")


    # # 방문한 리스트의 숫자
    # visited_num = [0]
    # # 정사각형을 하나씩 확인
    # for row in range(N):
    #     # 행이 짝수일 때
    #     if row % 2 == 1:
    #         # 오른쪽에서 왼쪽으로 확인
    #         for col in range(N - 1, - 1, -1):
    #             visited[N * row + N - col] = check_surrounding(col, row, board)
    #             visited_num.append(board[row][col])
    #     # 행이 홀수일 때
    #     else:
    #         # 왼쪽에서 오른쪽으로 확인
    #         for col in range(N):
    #             visited[N * row + col + 1] = check_surrounding(col, row, board)
    #             visited_num.append(board[row][col])
    #
    # # 최대 길이
    # max_len = 0
    # # 최대 길이의 시작과 끝
    # start = 0
    # end = 0
    # # 현재 길이
    # length = 0
    # # 시작하는 숫자
    # start_num = 0
    # # 시작, 끝, 길이를 저장하는 파일
    # answer = [0, 0, 0, 0]
    # # visited 표시
    # for i in range(len(visited)):
    #     # i가 0일 때는 의미 X
    #     if i == 0:
    #         continue
    #     # 현재 1일 때
    #     if visited[i] == 1:
    #         # 시작하는 점
    #         if visited[i - 1] == 0:
    #             start = i
    #             length = 0
    #             start_num = visited_num[i]
    #         # 마지막 숫자일 때 끝나지 않았을 때
    #         elif i == len(visited) - 1:
    #             length += 1
    #             end = i
    #             if max_len < length:
    #                 answer = [start, end, max_len, start_num]
    #
    #         # 그 외에는 모두 포함
    #         else:
    #             length += 1
    #     # 현재 0일 때
    #     elif visited[i] == 0:
    #         # 끝나는 점일 때
    #         if visited[i - 1] == 1:
    #             end = i
    #             length += 1
    #             if max_len < length:
    #                 max_len = length
    #                 answer = [start, end, max_len, start_num]
    #             elif max_len == length:
    #                 answer[3] = min(answer[3], start_num)
    #         # 그외는 아무 의미 없음
    #         else:
    #             continue


    # print(f"#{test_case} {answer[3]} {answer[2] + 1}")
