"""
Prime Generator
By: Akshay Sharma
Date: 23/7/16
"""
def sieve(n1, n2):
    if n2 == 0:
        return
    prime = [True]*(n2+1)
    prime[0] = prime[1] = False
    i = 2
    while i*i <= n2:
        if prime[i]:
            j = i*2
            while j <= n2:
                prime[j]=False
                j += i
        i += 1
    for k in range(n1, n2+1):
        if prime[k]:
            print(k)

N = eval((input()))
for l in range(N):
    intervals = list(map(int, input().split()))
    sieve(intervals[0], intervals[1])
    print("\n")
