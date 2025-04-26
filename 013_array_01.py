# 배열 원소의 최댓값을 구하는 함수 구현하기 p.77
from typing import Any, Sequence

def max_of(a : Sequence) -> Any :
    # 시퀀스형 a 원소의 최댓값을 반환
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]
    
    return maximum

if __name__ == "__main__" :
    print("배열의 원소를 구합니다.")
    num = int(input("원소 수를 입력하세요 : "))
    x = []
    
    for i in range(num) :
        x.append(int(input(f"x[{i}] 값을 입력 하세요 : ")))
    
    print(f"x의 최댓값은 {max_of(x)} 입니다.")
    
# from typing import Any, Sequence
# Any란 제약이 없는 임의의 자료형을 의미한다.            -> a에 어떤 자료형이 와도 다 받는다는 뜻
# Sequence는 시퀀스형(sequence type)을 의미한다.       -> 순서가 있는 자료형(인덱스로 접근할 수 있는 자료형)
# 시퀀스형에는 리스트(list)형, 바이트 배열(bytearry)형, 문자열(str)형, 튜플(tuple)형, 바이트열(byte)형이 있다.

# def max_of(a : Sequence) -> Any : 코드 해석
# 매개변수 a의 자료형은 Sequence이다.   -> 순서가 있는 자료형으로 받겠다.
# 이 함수가 리턴하는 값은 Any다.        -> 리턴값이 어떤 자료형이 올지 모르니 아무 자료형으로 반환하겠다.
# 이런 방식을 함수 어노테이션(Function Annotation)이라고 한다.
# -> 함수의 매개변수(입력값)와 리턴값(출력값)에 자료형 정보나 설명을 달아놓는 것

# if __name__ == "__main__" :
# 파이썬에서는 각 스크립트 프로그램을 모듈이라고 칭한다. 확장자를 제외한 파일 이름 자체를 모듈 이름으로 사용한다.
# 이 파일에서는 "013_array_01" 이 모듈 이름이다.
# __name__ 은 모듈 이름을 나타내는 변수
# 스크립트 프로그램이 직접 실행될때는 변수 __name__ 은 "__main__" 이다.
# 스크립트 프로그램이 임포트될 때 변수 __name__ 은 원래의 모듈 이름이다. => 이 파일이 아닌 다른 파일에서 임포트 될때는 "013_array_01" 이다.
# 그렇다면 다른 파일에서 이 코드를 임포트해서 실행시 13~21번 코드는 실행되지 않는다. if문에서 걸리기 때문.