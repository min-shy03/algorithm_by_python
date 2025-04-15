# 가우스의 덧셈 공식을 이용하여 n부터 m까지의 정수의 합을 구해보자

print("n부터 m까지의 정수의 합을 구합니다.")
n = int(input("n값을 입력하세요 : "))
m = int(input("m값을 입력하세요 : "))

# 숫자가 거꾸로 들어올 수도 있음 방지!
if n > m :
    n, m = m, n

# 먼저 1부터 m까지의 합을 구한다.
total_1 = m * (m + 1) // 2

# 그 후 1부터 n-1 까지의 값을 구한다.
total_2 = n * (n - 1) // 2

# 구한 두 값을 빼면 답이 나온다!
result = total_1 - total_2

print(result)