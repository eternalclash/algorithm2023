import math

def child_parent(num,parent) :
    if num == '':
        return True
    mid = len(num)//2
    me = num[mid]
    if me == '1' and parent == '0':
        return False
    else:
        return child_parent(num[:mid],me) and child

def check(sum):
    if num == 1:
        return 1
    num = bin(num)[2:]
    digit = 2 ** (int(math.log(len(num),2)) + 1) - 1
    num = "0" * (digit - len(num)) + num

    if num[len(num)//2] == '1' and child_parent(num,True):
        return 1
    else:
        return 0

def solution(numbers):
    answer =[]
    for num in numbers:
        answer.append(check(sum))
    return answer