'''
    2. 계산기 클래스 (Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 누적
                add_count, min_count, mul_count, div_count

        기능
            1. 생성자 __init__
                > 속성 만들기  (생성자에서 속성을 만든다 = 모든 인스턴스가 공통적으로 속성을 가진다.)
            2. 각 사칙연산을 계산하는 메서드 4개
                > 계산하고 싶은 2개의 값을 전달 받고, 계산 결과를 출력 (반환 X)
                    1 + 2 = 3
            3. 정보 출력(print_info)
                > 각 계산의 수행 횟수 출력

        ex) 덧셈 함수 3번 호출, 나눗셈 함수 2번 호출 후 print_info를 호출하면,
            1 + 2 = 3
            2 + 5 = 7
            10 / 2 = 5.0
            10 / 2 = 5.0
            3 + 9 = 12
            덧셈 : 3
            뺄셈 : 0
            곱셈 : 0
            나눗셈 : 2
'''
