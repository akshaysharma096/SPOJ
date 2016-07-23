"""
CharacterPatternACT4
By: Akshay Sharma
Date : 21/07/16
"""
t = int(input())
for cas in range(t):
    line = input();
    a = line.split(' ');
    l = int(a[0])
    c = int(a[1])
    h = int(a[2])
    w = int(a[3])
    row = l * (h + 1) + 1
    col = c * (w + 1) + 1
    for i in range(row):
        for j in range(col):
            if (0 == i % (h + 1) or 0 == j % (w + 1)):
                print('*', sep='', end='')
            else:
                print('.', sep='', end='')
        print()
    print("\n")