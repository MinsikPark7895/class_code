# 1065번

N = int(input())

result = 0

for i in range(1, N + 1):

    nums = []

    while i > 0:
        num = i % 10
        nums.append(num)
        i //= 10

    if 1 <= len(nums) <= 2:
        result += 1
    elif len(nums) > 2:
        diff = None
        for j in range(len(nums) - 1):
            if j == 0:
                diff = nums[j] - nums[j + 1]
            elif j == len(nums) - 2 and diff == nums[j] - nums[j + 1]:
                result += 1
            elif diff == nums[j] - nums[j+1]:
                continue

print(result)
