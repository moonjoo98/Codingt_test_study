# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

#solution 1
import sys

a = sys.stdin.readline().strip()

a_list= list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline().strip())
print(a_list.count(v))

# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())
# print(n_list.count(v))