#두 정수 A와 B를 입력받은 다음 A+B를 출력하는 프로그램을 작성하시오.
import sys
a,b= map(int,sys.stdin.readline().split())# 변수 타입이 문자열 형태로 저장되기 때문에 정수로 형 변환
print(a+b)