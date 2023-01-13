# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

#solutions 1 무식하게
import sys
a_list=[]
for i in range(9):
    a= int(sys.stdin.readline().strip())
    a_list.append(a)

sum_=sum(a_list)

for j in range(len(a_list)):
    for k in range(j+1,len(a_list)):
        if sum_ - (a_list[j]+a_list[k]) == 100:
            one=a_list[j]
            two=a_list[k]
a_list.remove(one)
a_list.remove(two)
a_list.sort()
for z in a_list:
    print(z)

# solutions 2 itertools 사용 시간은 더 오래걸린다..
import itertools
import sys
a_list = [int(sys.stdin.readline().strip()) for _ in range(9)]

for i in itertools.combinations(a_list, 7):  # 해당 배열을 7명 중복없이 뽑아준다.
    if sum(i) == 100:  
        for j in sorted(i):  
            print(j)
        break 
        
