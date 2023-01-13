# 동규는 세수를 하다가 정렬이 하고싶어졌다.
# 숫자 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어 졌다.
# 숫자 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

# solution 1
import sys
a,b,c = map(int,sys.stdin.readline().split())
d=min([a,b,c])
f=max([a,b,c])
e=a+b+c-d-f
print(d,e,f,sep=' ')

# solution 2
import sys
a_list= list(map(int,sys.stdin.readline().split()))
a_list.sort()
print(a_list[0],a_list[1],a_list[2])
