# 에라토스테네스의 체를 이용하여 n 값 이하의 소수 구하기
# 이 버전은 리스트를 n값만큼 생성하기 때문에 공간 복잡도 측면에선 매우 부적절하다!

def prime(n) :
    # 0을 포함한 n + 1 값만큼 리스트 생성
    lst = [True] * (n + 1)
    
    lst[0] = lst[1] = False
    
    # 루트 n값 까지만 돌아도 전체 소수를 걸러낼 수 있다. => 15번 줄 코드와 연관 있음 
    # 만약 i 값이 루트 n값보다 크다 가정했을 때, i * i는 n 값보다 커서 볼 필요도 없고
    # 그 외의 합성수는 그 i값에 도달하기 전에 다 걸러지기 때문이다.
    for i in range(2, int(n ** 0.5) + 1) :
        # 만약 걸러지지 않은 수라면 실행 => 실행 시간을 대폭 줄여줌
        if lst[i] :
            # i * i 부터 실행하는 이유 = 그 전의 숫자들 중 합성수는 해당 i값에 도달하기 전의 소수의 배수로 다 지웠음
            # n + 1로 n값까지 확인
            # i의 배수 만큼 확인해야하기 때문에 i씩 증가
            for j in range(i * i, n + 1, i) :
                if lst[j] :
                    lst[j] = False
                
    return [idx for idx, val in enumerate(lst) if val]

print(prime(30))