#20221576 김시온
m = [[1, 2], [3, 4], [5, 6], [7, 8]]

print("원 행렬(m) 출력:")
for i in range(4):
    for j in range(2):
        print(m[i][j], end=' ')
    print()

print()
print("전치 행렬 출력:")
for i in range(2):
    for j in range(4):
        print(m[j][i], end=' ')
    print()