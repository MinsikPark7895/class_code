import sys
sys.stdin = open("price_input.txt", "r")

T = int(input())

def change_trial(number, trials):
    if trials == 0:
        return number

    nums = []
    for num in nums:
        nums.append(int(num))
    finding_num = max(nums)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == finding_num:
            if nums[0] != finding_num:
                nums[0], nums[i] = nums[i], nums[0]
                next_num = 0
                n = 0
                while n < len(nums):
                    next_num *= 10
                    next_num += nums[n]
                    n += 1
                change_trial(str(next_num)[1:], trials - 1)
                break



for test_case in range(1, T + 1):

    number, trials = input().split()

    num_list = []
    for let in number:
        num_list.append(int(let))

    largest = sorted(num_list, reverse=True)

    change_trial(number, trials)

