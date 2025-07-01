# 직사각형 넓이로 변의 길이 구하기

area = int(input("직사각형 넓이 입력 : "))

# for i in range(1, area + 1) :
#     # i가 가장 긴 변의 길이가 되면 종료
#     # 중복 결과 방지 ex) 3 x 12나 12 x 3이나 결과 값은 같음 굳이 출력할 이유 x 
#     if i * i > area :
#         break
    
#     # 곱했을 때 area가 되는 약수들만 확인하면 됨. 그 외엔 continue로 스킵
#     if area % i :
#         continue
    
#     # 짧은 변과 긴 변의 순서로 출력
#     print(f"{i} x {area // i}")

# 범위를 더 짧게 줄여서 쓸 수 있다!
for i in range(1, int(area ** 0.5) + 1) :
    if area % i :
        continue
    print(f"{i} x {area // i}")