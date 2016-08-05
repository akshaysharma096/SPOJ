"""
CMPLS
By: Akshay Sharma
Date : 05/08/16
"""
def predict(point, arr):
    leng = len(arr)
    result = 0
    for k in range(leng):
        l = 1
        d = 1
        for j in range(leng):
            if j != k:
                temp = point - j
                l *= temp
                temp = k - j
                d *= temp
        result += (l / d) * arr[k]
    return int(result)


N = eval(input())
for i in range(N):
    data = list(map(eval, input().split()))
    arr = list(map(eval, input().split()))
    n = data[0]
    c = data[1]
    for p in range(c):
        print(predict(n + p, arr),end = " ")
    print("\n")
