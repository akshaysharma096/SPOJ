"""
Character PatternACT2
By: Akshay Sharma
Date: 21/07/16
"""
N = int(input())
for i in range(N):
    numbers = list(map(int, input().split()))
    rows = numbers[0]
    cols = numbers[1]
    for j in range(rows):
        star = "*"
        dot = "."
        temp_string = ""
        for k in range(cols):
            if j == 0 or j == rows-1 or k == 0 or k == cols-1:
                temp_string += star
            else:
                temp_string += dot
        print(temp_string)
    print("\n")

