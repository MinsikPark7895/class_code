# arr = ['A', 'B', 'C', 'D', 'E']
#
# n = len(arr)
#
# def get_sub(tar):
#     subsets = []
#     for i in range(n):
#         if tar & 0x1:
#             subsets.append(arr[i])
#         tar >>= 1
#     return subsets
#
# for target in range(1 << n):
#     subset = get_sub(target)
#     if subset

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    # for i in range(n):
    #     if tar & 0x1:
    #         cnt += 1
    #     tar >>= 1

    # 위와 같은 코드임
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1
    return cnt



# 모든 부분집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
# 모든 부분 집합을 확인
for target in range(1 << n):
    # 만약, 원소의 개수가 2개 이상이면 answer ++
    if get_count(target) >= 2:
        answer += 1

print(answer)


