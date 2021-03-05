# koreais_module.py

# 모듈의 코드 작성

# 변수
str1 = "koreais_module의 문자열~!"

# 함수
def add(a, b):
    return a+b

def mul(a, b):
    return a*b

# 클래스
class Dog:
    def __init__(self, name):
        self.name = name
    def cry(self):
        print(f"{self.name} : 멍멍!")



'''
    파이썬에서 기본적으로 제공하는 변수
        > __name__
        > 문자열을 들고 있는 변수

    내가 직접 실행 : "__main__"
    다른 소스 파일 import: import한 이름 그대로 (문자열)

'''

if __name__ == __main__:
    print("__name__=", __name__)
    print("나는 koreais_module의 print()함수!")











