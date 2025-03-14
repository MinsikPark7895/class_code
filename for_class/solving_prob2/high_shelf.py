import sys
sys.stdin = open("high_input.txt", "r")

T = int(input())

def check_sum(heights, wanted_height):
    global total_height
    if total_height >= wanted_height:

        return


for test_case in range(1, T + 1):

    N, B = map(int, input().split())

    heights = list(map(int, input().split()))
    #
    # total_subsets = []
    # # for i in range(2**N)
    # for i in range(1<<N):
    #     subset = []
    #     for j in range(N):
    #         if i & (1<<j):
    #             subset.append(heights[j])
    #     total_subsets.append(subset)
    #
    # larger_subsets = []
    # for subset in total_subsets:
    #     if sum(subset) >= B:
    #         larger_subsets.append(sum(subset) - B)
    #
    # print(f"#{test_case} {min(larger_subsets)}")