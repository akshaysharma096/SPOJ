"""
Life the universe and everything
By: Akshay Sharma
Date : 23/7/16
"""
from collections import deque
queue = deque([])
while True:
    number = eval(input())
    if number == 42:
        while len(queue) != 0:
            print(queue.popleft())
        break
    else:
        queue.append(number)
