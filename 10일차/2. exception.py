# exception.py


'''
    [예외처리]
        개발자가 의도하지 않은 오류 발생에 대한 처리
            >프로그램 오류가 발생하면 프로그램이 종료된다.
            (다음 코드 실행x)


    try, except문

    try:
        기본 수행문 (무조건 진입해서 수행)
    except:
        오류 발생 시 수행되는 수행문

        
'''

# 예외처리

'''

try:
    input_num = int(input("숫자 입력 : "))
    print("결과 :", input_num)
except:
    print("숫자를 입력하세요!")
finally:
    print("예외처리 끝!")
'''  

# (1) try문 : 오류가 발생되는 '예상' 지역
# (2) except문 : 오류 발생 시 '처리' 지역
#   > 오류 발생 시 오류가 발생한 코드에서 except문으로 점프
#   > 오류가 발생하지 않으면 except문은 수행되지 않고 try문이 끝난다.

# finally문 : 마지막에 무조건 수행되는 구문
# > 정상/오류 구분 없이 무언가 마무리할 코드가 있을 때 사용

# 오류 구분하기
"""
try:
    try:
        print(abc)
    except:
        print("변수명이 잘못되었습니다.")
    print(abc)
    num1, num2 = map(int, input("두 수 입력 : ").split())
    print("나눈 결과 :", num1 / num2)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 정확히 입력하세요!")

except:
    print("오류 발생!")
"""

'''
가위 바위 보 게임 만들기.


=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

이겼습니다. ^^

---------------------------		

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 2     

졌습니다. ㅜㅜ

------------------------------

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 3     

비겼습니다. -_-


// 기능 추가 : 컴퓨터가 선택한 숫자 출력.
// 예외처리 : 1, 2, 3 이외의 숫자가 들어가면 에러메시지 출력 후 복귀(게임 지속)
// 'x' or 'X' 를 입력 받으면 종료. x외의 문자 입력시에도 에러메세지 출력후 복귀.
'''

import random

while True:

    user = input("1. 가위 / 2. 바위 / 3. 보 ) : ")
    com = random.randint(1, 3)

    if user == "x" or user == "X":
        break

    try:
        user = int(user)
    except:
        print("문자를 잘못 입력하였습니다. x 또는 X를 입력하세요!")
        continue

    if user > 3 or user < 1:
        print("1~3까지 숫자를 입력하세요!")
        continue


    result = user - com
    if result == 0:
        print("비겼습니다. com =", com)
    elif result == -2 or result == 1:
        print("이겼습니다. com =", com)
    elif result == -1 or result == 2:
        print("졌습니다. com =", com)

    










    
