# 10580 전봇대

"""
교차점이 발생하는 경우는 2가지
- 새로운 선을 추가할 때(교차점이 발생하는 케이스)
-> 새로운 선 추가할 때마다 비교를 진행
- 기존 선과 비교
    1. 시작점이 높으며, 도착점이 낮음
    2. 시작점이 낮으며, 도착점이 높음

"""
import sys
sys.stdin = open("candy_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    wires = []
    answer_count = 0

    for _ in range(N):
        start, end = map(int, input().split())

        for prev_start, prev_end in wires:
            if start > prev_start and end < prev_end:
                answer_count += 1
            elif start < prev_start and end > prev_end:
                answer_count += 1

        wires.append((start, end))
    print(f'#{test_case} {answer_count}')
