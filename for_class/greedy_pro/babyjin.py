import sys
sys.stdin = open("babyjin_input.txt", "r")

T = int(input())

# 차이가 동일한 카드
def card_run(input_list):
    result = False
    N = len(input_list)
    # 길이 3 이하 고려 X
    if N < 3:
        return result
    # 고려
    else:
        input_list.sort()
        new_list = list(set(input_list))

        for i in range(len(new_list) - 2):
            if new_list[i] + 1 == new_list[i + 1] and new_list[i + 1] + 1 == new_list[i + 2]:
                result = True
                break

    return result


# 3개 이상 같은 숫자
def card_triplet(input_list):
    input_list.sort
    M = len(input_list)
    result = False

    if M >= 3:
        for j in range(M - 2):
            if input_list[j] == input_list[j + 1] == input_list[j + 2]:
                result = True
                break

    return result


for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    player1 = []
    player2 = []

    winner = 0
    # 게임 진행
    for i in range(len(arr)):
        if i % 2 == 0:
            player1.append(arr[i])
            if card_run(player1) or card_triplet(player1):
                winner = 1
                break
        else:
            player2.append(arr[i])
            if card_run(player2) or card_triplet(player2):
                winner = 2
                break

    print(f"#{test_case} {winner}")



