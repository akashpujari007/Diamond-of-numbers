n = int(input())
n1 = n
n2 = n1 - 1
for row in range(1, n1 + 1):
    for spaces in range(0, n - row):
        print(' ', end='')
    for col in range(row, 0, -1):
        print(col, end='')
    for col in range(2, row+1):
        print(col, end='')
    print()

for row in range(1, n2+1):
    for spaces in range(0, row):
        print(' ', end='')
    for col in range(n2-row+1, 0, -1):
        print(col, end='')
    for col in range(2, n2-row+2):
        print(col, end='')
    print()