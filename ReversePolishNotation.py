def infix_to_postfix(expression):
    precedence = {'(': -1, '+': 0, '-': 1, '*': 2, '/': 3, '^': 4}
    stack = []
    for i in range(len(expression)):
        if expression[i] == ')':
            while stack[len(stack) - 1] != '(':
                print(stack.pop(), end="")
            if len(stack) != 0:
                stack.pop()
        elif expression[i] not in precedence:
            print(expression[i], end="")
        else:
            if len(stack) == 0 or precedence[expression[i]] > precedence[stack[len(stack) - 1]]:
                stack.append(expression[i])
            else:
                while len(stack) != 0 and precedence[expression[i]] > precedence[stack[len(stack) - 1]]:
                    popped = stack.pop()
                    if popped != '(':
                        print(popped, end="")
                stack.append(expression[i])
    while len(stack) != 0:
        print(stack.pop(), end="")


N = eval(input())
for i in range(N):
    temp = input()
    infix_to_postfix(temp)
    print()
