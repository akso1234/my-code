#20221576 김시온
import random

ran_list = []
for i in range(10):
    ran_list.append(random.randint(1, 101))
print("리스트:", ran_list)

ran_tuple = tuple(ran_list)
print("튜플:", ran_tuple)
print("튜플 정렬된 리스트", sorted(ran_tuple))

print()
print("합:",sum(ran_tuple), end=', ')
print("항목수:", len(ran_tuple))
print("최대:", max(ran_tuple), end=', ')
print("최소:", min(ran_tuple), end=', ')
print("평균:", sum(ran_tuple) / 10)