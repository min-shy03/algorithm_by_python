# 1부터 n 까지의 정수의 합을 구하고 싶을 때
# 반복문을 쓰는 것은 프로그램 실행 속도도 오래걸리고 좋지 않다.
# 가우스의 덧셈 수식을 이용하여 똑똑하게 풀어보자.

n = int(input("1부터 n까지 정수를 구해보자 n값을 입력하라 : "))

# 가우스의 덧셈 수식 -> 이걸 어떻게 초등학교 때 발견하지? 존경스러워지는 부분이다.
total = n * (n + 1) // 2

print(total)