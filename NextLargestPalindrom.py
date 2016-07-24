"""
SPOJ_PALIN
By : Akshay Sharma
Date: 24/07/16
"""


def next_palindrome(number):
    numbers = [int(i) for i in str(number)]
    if all_nine(numbers):
        return number + 2
    l = len(numbers)
    str_number = str(number)
    mid = l // 2
    if l % 2 == 0:
        left = str_number[:mid]
        right = left[::-1]
        new_string = "%s%s" % (left, right)
        new_number = int(new_string)
        if new_number > number:
            return new_number
        else:
            return work([int(i) for i in str(new_number)], mid - 1, mid)

    else:
        left = str_number[:mid]
        middle = str(numbers[mid])
        right = left[::-1]
        new_string = "%s%s%s" % (left, middle, right)
        new_number = int(new_string)
        if new_number > number:
            return new_number
        else:
            return work([int(i) for i in str(new_number)], mid, mid)


def work(numbers, start, end):
    if start < 0:
        numbers[len(numbers) - 1] = 1
        numbers[0] = 1
        new_string = ''.join(map(str, numbers))
        return int(new_string)
    elif numbers[start] < 9:
        numbers[start] += 1
        numbers[end] = numbers[start]
        new_string = ''.join(map(str, numbers))
        return int(new_string)
    else:
        numbers[start] = 0
        numbers[end] = 0
        return work(numbers, start - 1, end + 1)


def all_nine(numbers):
    for j in numbers:
        if j != 9:
            return False
    return True


N = eval(input())
for i in range(N):
    data = eval(input())
    print(next_palindrome(data))
