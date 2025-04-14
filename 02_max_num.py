# 세 정수의 최댓값 찾기 알고리즘
def maximum(a,b,c) :
    maximum = a
    
    if b > maximum :
        maximum = b
    
    if c > maximum :
        maximum = c
    
    return maximum

print(maximum(1,3,2))