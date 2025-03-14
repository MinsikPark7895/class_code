# 20551번 증가하는 사탕수열

# 사탕을 담은 상자
# A, B, C 개
# 순증가하길 원한다


# 내 설계
# - 두번째 상자
    # - 세번째 상자보다 작게 만들자
# - 첫번째 상자
    # - 두번째 상자보다 작게 만들자

# 설계 시작
"""
- 자료구조
- 3개의 숫자 + 먹은 개수만 저장하면 끝
- 리스트 vs A,B, C 저장

- 알고리즘
- 불가능한 케이스
    - B가 2보다 작은 경우
    - C가 3보다 작은 경우
- B는 C보다 작아야 한다
- B를 C보다 작을 때까지 하나씩 감소
- [검증] 사탕의 개수가 많으면, 시간 초과 가능성
- 3000까지니 가능하다
- B = C -1로 만들어준다


"""

import sys
sys.stdin = open("candy_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    # 불가능한 케이스를 미리 없애자
    if B < 2 or C < 3:
        print(f"#{test_case} -1")
        continue

    eat_count = 0
    # B가 C 이상이라면, B = C -1 로 만들자
    if B >= C:
        eat_count += B - (C - 1)
        B = C - 1
    # A가 B 이상이라면, a = B -1
    if A >= B:
        eat_count += A - (B - 1)
        A = B - 1

    print(f"#{test_case} {eat_count}")
