'''
가위 바위 보 게임 만들기.

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

이겼습니다. ^^

---------------------------		

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

졌습니다. ㅜㅜ

------------------------------

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

비겼습니다. -_-


// 기능 추가 : 컴퓨터가 선택한 숫자 출력.
// 예외처리 : 1, 2, 3 이외의 숫자가 들어가면 에러메시지 출력 후 복귀(게임 지속)
// 'x' or 'X' 를 입력 받으면 종료. x외의 문자 입력시에도 에러메세지 출력후 복귀.
'''

import random

while True:
    
    user = input("1. 가위 / 2. 바위 / 3. 보 : ")
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

    














