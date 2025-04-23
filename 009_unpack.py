# 언팩(unpack)
# 좌변에 여러 개의 변수를 놓고 우변에 리스트나 튜플을 두어 
# 우변의 원소의 값을 좌변의 변수에 한 번에 대입하는 방법 

# x = [1,2,3]
# a,b,c = x
# a,b,c >> (1,2,3)

# 좌변의 변수 갯수와 우변 리스트의 길이가 맞지 않으면 오류 발생!! -> 당연하다.

# x = [1,2,3]
# a, b = x          -> ValueError: too many values to unpack (expected 2)
# a, b, c, d = x    -> ValueError: not enough values to unpack (expected 4, got 3)

# 하지만 리스트의 길이가 변수의 갯수보다 많을 때 분할해서 넣고싶다면 * 사용하면 된다!
# 변수가 리스트의 길이보다 많을 경우는 답 없음.

# x = [1, 2, 3, 4, 5]
# a, *b = x              # a = 1, b = [2, 3, 4, 5]
# a, b, *c = x           # a = 1, b = 2, c = [3, 4, 5]
# *a, b = x              # a = [1, 2, 3, 4], b = 5