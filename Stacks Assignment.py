"""
Author: Electra Bree
Assignment related to stacks
"""

class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)                

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)        

    def __str__(self):
        return 'Stack: ' + str(self.__items)
        
    def reverse(self):
        return self.__items.sort(reverse=True)

# Creates a new stack where the top of the stack is the parameter value, and all subsequent values on the stack decrease by 1 until the bottom value which equals to 1
def countup_stack(number):
    stack = Stack()
    for element in range(1, number + 1):
        stack.push(element)
    return stack

# Takes a list of operators and operands (all strings), representing a valid postfix expression, and evaluates it
def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2
    else:
        return number1 ** number2

def evaluate_postfix(postfix_list):
    stack = Stack()
    for element in postfix_list:
        try:
            stack.push(int(element))
        except ValueError:
            top = stack.pop()
            below = stack.pop()
            result = compute(below, top, element)
            stack.push(result)
    return stack.peek()

# Reads n (number) integers, stores all integers in a stack and prints them in reverse order.
# If consecutive numbers are the same, only one of them will be stored in the stack.
def read_reverse_integers(n):
    stack = Stack()
    previous = None
    for time in range(n):
        integer = int(input("Enter an integer: "))
        if integer != previous:
            stack.push(integer)
        previous = integer
    for element in range(stack.size()):
        if stack.is_empty() == False:
            print(stack.pop())

# Returns the length of the longest valid (balanced) parentheses substring
def get_longest_run(text):
    stack = Stack()
    stack.push(-1)
    result = 0
    for index in range(len(text)):
        if text[index] == "(":
            stack.push(index)
        if text[index] == ")":
            stack.pop()
            if stack.is_empty() == False: #not empty
                length =  index - stack.peek()
                if length > result:
                    result = length
            else:
                stack.push(index)
    return result
