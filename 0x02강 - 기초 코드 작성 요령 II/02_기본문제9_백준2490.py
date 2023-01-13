#우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 
#네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

# solution 1

import sys

for i in range(3):
    a,b,c,d=map(int,sys.stdin.readline().split())

    if a+b+c+d == 3:
        print('A')
    elif a+b+c+d == 2:
        print('B')
    elif a+b+c+d == 1:
        print('C')
    elif a+b+c+d == 0:
        print('D')
    else:
        print('E')

# solution 2
for _ in range(3):
    s = sum(map(int, input().split()))
    if s == 4:
        print("E")
    elif s == 3:
        print("A")
    elif s == 2:
        print("B")
    elif s == 1:
        print("C")
    else:
        print("D")