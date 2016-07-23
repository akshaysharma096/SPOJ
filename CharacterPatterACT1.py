N = int(input())
for i in range(N):
    rows, cols = input().split()
    rows = int(rows)
    cols = int(cols)
    for j in range(rows):
        if j % 2 == 0:
            first = '*'
            second = '.'
        else:
            first = '.'
            second = '*'
        temp_string = ''
        for k in range(cols):
            if k % 2 == 0:
                temp_string += first
            else:
                temp_string += second
        print(temp_string)
    print("\n")




