import sys
import math
import csv
import pandas as pd


#1주차 : 강동구를 중심을 기준으로 각 동까지의 거리 data 정리 위도와 경도에 따른 거리 계산식산출
#2주차 : 배달 지역 동 작성 시 거리 산출 코딩

#f = open ('town_data.csv', 'r')
#town = [‘암사동’, ‘천호동’, ‘성내동’, ‘길동’, ‘상일동’, ‘둔촌동’, ‘명일동’, ‘고덕동’]

town_data[towndata["동이름"]=="암사동"]

input ('동이름을 입력하세요')


x1,y1,z1 = input ('a지역 위도 도분초입력')
x2,y2,z2 = input ('b지역 위도 도분초입력')

a1,b1,c1 = input ('a지역 경도 도분초입력')
a2,b2,c2 = input ('b지역 경도 도분초입력')

111*(x1-x2) + 1.85*(y1-y2) + 0.031*(z1-z2) = lat # A지역과 B지역의 위도 차이 구하기
88.8*(a1-a2) + 1.48*(b1-b2) + 0.025*(c1-c2) = log # A지역과 B지역의 경도 차이 구하기

Straight_Distance = lat^2+log^2
math.sqrt(Straight_Distance)
print('배달거리는 ', Straight_Distance, '입니다.')

