#1546
import sys

point = int(input()) 
point_list = list(map(int,input().split())) 
max_point = max(point_list) 
average = 0

for i in range(point):
    point_list[i] = point_list[i]/max_point*100
    average += point_list[i]
average = sum(point_list)/point

print("%.2f"%average)