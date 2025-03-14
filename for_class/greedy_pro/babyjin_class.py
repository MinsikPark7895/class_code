# run : 1, 2, 3과 같이 연속된 숫자 3개를 보유하고 있다면 run
# triplet : 똑같은 숫자 3개를 보유하고 있다면 triplet
# 정렬된 카드들을 확인하는 경우
# idx를 기준을 하면 잘못 판단할 수 있으니
# 카드의 개수를 받아서 판단하는 방식으로 진행

def baby_gin(card_cnt):
    # triple부터 판단
    for i in range(10):
        # 한 종류의 카드가 3장 이상아면 triplet
        if card_cnt[i] > 2:
            return True

    # 그 다음 run 판단
    for i in range(8):
        # i부터 총 3장의 카드가 1장 이상이면 run
        if card_cnt[i] > 0 and card_cnt[i + 1] > 0 and card_cnt[i + 2] > 0:
            return True
    # 둘다 아니면
    return False

T = int(input())

for test_case in range(1, T + 1):
    # 전체 카드를 먼저 받아둔다
    cards = list(map(int, input().split()))
    # 각 플레이어가 가진 카드의 개수를 파악하는 리스트를 준비한다
    card_cnt_1 = [0 for _ in range(10)]
    card_cnt_2 = [0 for _ in range(10)]

    # 기본적을 run이든 triplet이든 3장은 있어야 한다
    # -> 3장이 되기 전에는 판단할 필요가 없다
    # 첫 두장은 그냥 준다.
    for i in range(2):
        card_cnt_1[cards[i * 2]] += 1
        card_cnt_2[cards[i * 2 + 1]] += 1

    # 결과를 저장하는 변수를 준비
    result = 0
    # 나머지 카드를 순서대로 배분하면서,
    for i in range(2, 6):
        card_cnt_1[cards[i * 2]] += 1
        card_cnt_2[cards[i * 2 + 1]] += 1
        # 1번이 점수를 냈는지
        if baby_gin(card_cnt_1):
            result = 1
        # 2번이 점수를 냈는지
        elif baby_gin(card_cnt_2):
            result = 2

        # 결과가 나왔으면 반복을 더 할 필요가 없다
        if result:
            break

        # 그 결과 누가 이겼는지를 판단한다.
    print(f"#{test_case} {result}")

