rsum = []
csum = []
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    number = 0
    for j in range(3):
        number = number + data[i][j]
    rsum.append(number)

for i in range(3):
    number = 0
    for j in range(3):
        number = number + data[j][i]
    csum.append(number)

print("각 행의 합:", rsum)
print("각 열의 합:", csum)
