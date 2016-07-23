"""
Character Patter ACT 3
By: Akshay Sharam
Date: 21/07/16
"""
N = int(input())
for i in range(N):
    numbers = list(map(int, input().split()))
    rows = numbers[0]
    cols = numbers[1]
    for j in range(3*rows+1):
        if j % 3 == 0:
            print("*"*(3*cols+1))
        else:
            star = "*"
            dot = "."
            temp_string = ""
            for k in range(3*cols+1):
                if k % 3 == 0:
                    temp_string += star
                else:
                    temp_string += dot
            print(temp_string)
    print("\n")