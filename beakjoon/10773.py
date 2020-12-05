#10773
import sys

books = int(input())
stack_list = []

for i in range(stack_list):
    num = int(input())
    if(num == 0):
        stack_list.pop()
    else:
        stack_list.append(stack_list)

print(sum(stack_list))