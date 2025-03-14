# 주사위 3개를 던져 나올 수 잇는 모든 조합을 출력
# 종료조건: 주사위 3개를 던졌을 때
# branch: 1~6 숫자
N = 3
path = []

def recur(cnt, start):
    if cnt == N:
        print(path)
        return

    for i in range(start,  7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()

recur(0, 1)



