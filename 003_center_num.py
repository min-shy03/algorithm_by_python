# 세 정수의 중앙값 찾기 알고리즘
def center(a,b,c) :
    # a가 b 이상일 때
    if a >= b :
        # b가 c 이상일 경우 b는 중앙값
        if b >= c :
            return b
        # c가 a 이상일 경우 a는 중앙값
        elif c >= a :
            return a
        # 그 외엔 c가 중앙값
        else :
            return c
    # a >= b가 거짓이라면 b > a 임으로 a가 c보다 크면 a는 중앙값 
    elif a > c :
        return a
    # 위 식까지 통과됐다면 b > a , c >= a 임으로 b > c 라면 c는 중앙값
    elif b > c :
        return c
    # 그 외는 b가 중앙값
    else : 
        return b

print(center(412,4215,432))