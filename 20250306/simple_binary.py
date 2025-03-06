#1.
import sys
sys.stdin = open("simple_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # N: 배열의 세로 크기
    # M: 가로 크기 M
    N, M = map(int, input().split())
    # 들어온 2차원 배열
    cryptography = [input() for _ in range(N)]
    # 진짜 해독해야하는 문자
    found_code = None

    # 현재 행 확인
    for row in range(N):
        # 현재 열 확인
        for col in range(M - 1, -1, -1):
            # 오른쪽에서 암호 해독 필요부분이 나오면
            if cryptography[row][col] == "1":
                # 현재 위치 포함 앞으로 56개의 bit를 해독 코드에 보냄
                found_code = cryptography[row][col - 55: col + 1]
                break
        # 암호문이 모든 줄에서 일정할까?
        # found_code에 값이 있으면 break
        if found_code:
            break

    # 해독문
    num_code = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9,
    }

    # 숫자를 넣어야 하는 리스트
    real_code = []

    # 각 숫자를 넣는 코드
    for i in range(8):
        code_now = found_code[i*7 : i*7 + 7]
        changed_code = num_code[code_now]
        real_code.append(changed_code)

    odd = 0
    even = 0
    # 각 홀수와 짝수에 따른 암호코드 확인
    for i in range(8):
        if i % 2 == 0:
            odd += 3 * real_code[i]
        else:
            even += real_code[i]

    total = odd + even
    answer = 0

    if total % 10 == 0:
        answer = sum(real_code)



    print(f"#{test_case} {answer}")


