people = [15, 30, 50, 10]
n = len(people)

# 규칙, 최소 시간인 사람부터 화장실로 들어가자
people.sort()

total_time = 0
remain_people = n - 1

for turn in range(n):
    time = people[turn]
    total_time += remain_people * time
    remain_people -= 1

print(total_time)
