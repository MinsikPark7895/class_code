# 카드 두장을 골라서 교환하는 함수
# 몇번째 교환이냐 (몇번이나 더 교환해야 하느냐)만 있어도 된다
def swap(rep):
    # 교환 횟수를 맞췄다
    if rep == n:
        global max_prize
        # 현재 카드의 상태를 바탕으로 상금을 추출
        prize = int(''.join(cards))
        # 최대값과 비교한다
        max_prize = max(max_prize, prize)
        return
    # 교환횟수가 남았으면 대상을 고르고 교환
    # 첫번째 카드 선택
    # 0 ~ 4
    for i in range(len(cards) - 1):
        # 두번째 카드 선택
        for j in range(i + 1, len(cards)):
            # 교체해본다
            cards[i], cards[j] = cards[j], cards[i]
            # 만약 같은 교환횟수에 똑같은 카드 배열이 없었다면,
            prize = int(''.join(cards))
            if prize not in memo[rep]:
                # 지금 도달 정보를 작성해주고,
                memo[rep].add(prize)
                # 다음 교체로 넘어간다
                swap(rep + 1)
            # 되돌린다
            cards[i], cards[j] = cards[j], cards[i]

T = int(input())

for test_case in range(1, T +1):
    cards, n = input().split()

    cards = list(cards)
    # 그래야 정수로 변환이 편해서
    # print(int(''.join(cards)))
    n = int(n)
    # 재귀적으로 카드를 골라서 교환하는 함수를 만들고 호출하자
    max_prize = 0
    # 교환 횟수당 등장한 카드 조합을 파악하기 위한 메모를 만들자
    # memo[i]: i번 교환한 다음 등장했던 숫자들의 집합
    memo = [set() for _ in range(n)]
    swap(0)
    print(f"#{test_case} {max_prize}")


