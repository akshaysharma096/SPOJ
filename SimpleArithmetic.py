"""
Simple Arithmetic
By: Akshay Sharma
Date:
"""


def output(expression):
    if '+' in expression:
        add(expression)
    elif '-' in expression:
        sub(expression)
    elif '*' in expression:
        multiply(expression)


def multiply(expression):
    expression_list = expression.split("*")
    int_1 = int(expression_list[0])
    int_2 = int(expression_list[1])
    result_str = str(int_1 * int_2)
    str_1 = expression_list[0]
    str_2 = expression_list[1]
    str_2 = "*%s" % str_2
    l_2 = max(len(str_2), len(str(int(expression_list[1][-1]) * int_1)))
    l = max(len(result_str),l_2)
    dashes_1 = "-" * l_2
    print(str_1.rjust(l, " "), str_2.rjust(l, " "), dashes_1.rjust(l, " "), sep="\n")
    i = len(expression_list[1]) - 1
    j = 0
    while i >= 0:
        digit = int(expression_list[1][i])
        answer = str(int_1 * digit)
        print(answer.rjust(l - j), " ")
        i -= 1
        j += 1
    if j == 1:
        return
    print(("-"*len(result_str)).rjust(l, " "), result_str.rjust(l, " "), sep="\n")


def add(expression):
    expression_list = expression.split("+")
    str_1 = expression_list[0]
    str_2 = expression_list[1]
    add_string = "+%s" % str_2
    max_l = max(len(str_1), len(add_string))
    result = int(str_1) + int(str_2)
    print(str_1.rjust(max_l, " "), add_string.rjust(max_l, " "), "-" * max_l, str(result).rjust(max_l, " "), sep="\n")


def sub(expression):
    expression_list = expression.split("-")
    str_1 = expression_list[0]
    str_2 = expression_list[1]
    int_1 = 0
    int_2 = 0

    if int(str_1) > int(str_2):
        int_1, int_2 = int(str_1), int(str_2)
    else:
        int_1, int_2 = int(str_2), int(str_1)
    g = str(int_1)
    l = str(int_2)
    sub_string = "-%s" % l
    max_l = max(len(g), len(sub_string))
    result = str(int_1 - int_2)
    print(g.rjust(max_l, " "), sub_string.rjust(max_l, " "), "-" * max_l, result.rjust(max_l, " "), sep="\n")


N = eval(input())
for i in range(N):
    input_str = input()
    output(input_str)
    print()
