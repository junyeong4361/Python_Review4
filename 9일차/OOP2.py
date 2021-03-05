# OOP2.py

'''
    [변수와 메서드 종류]
        - 클래스 변수
            1. 클래스 내부 코드에 생성
            2. 클래스 메서드에서 생성
            3. 클래스 코드 바깥에서 클래스명을 통해 생성

        - 인스턴스 변수
            1. 생성자에서 생성 (모든 인스턴스가 공통적으로 생성)
            2. 인스턴스 메서드에서 생성 (해당 인스턴스 메서드를 호출한 인스턴스만 생성)
            3. 클래스 코드 바깥에서 인스턴스명을 통해 생성 (해당 인스턴스에만 생성)

        * 클래스 변수는 한번 만들어지면 '클래스'나 '인스턴스'가 접근 가능하다.
          인스턴스 변수는 인스턴스별로 독립적으로 생성(클래스명으로 사용 불가)

        - 클래스 메서드
            클래스나 인스턴스가 호출 가능

        - 인스턴스 메서드
            인스턴스를 통해서만 호출 가능 (self에 인스턴스가 대입되어야 한다.)
    
'''

class Car:
    engine = "2000cc" # 클래스 변수

    @classmethod # 장식자(데코레이터) : 이게 있어야만 클래스 메서드 
    def clsMethod(self):
        print("클래스 메서드")
        self.value = "클래스변수"

    def instMethod(self):
        print("인스턴스 메서드")

# class 클래스명:
#   변수명
#   @classmethod
#   def 임의의문자1(self):
#       print("~!!")
#       self.value = "zzff"

#   def 임의의문자2(self):
#       print("!@!@")




print(Car.engine)


car1 = Car()

print(car1.engine)
# 클래스변수는 클래스명, 인스턴스명으로 사용 가능


Car.clsMethod()
print(Car.value)
print(car1.value)
# 인스턴스명으로 클래스변수, 클래스 메서드 사용 가능
print()

#Car.instMethod()
car1.power = True
#print(Car.power)
# 클래스명으로는 인스턴스 메서드, 인스턴스 변수 사용 불가능
print()



'''
    [외부 접근 제어]
        외부 = 클래스가 정의된 코드 바깥

        public : 외부 접근 허용 - 이름 지을 때 그냥 지으면 된다. (변수/메서드)
        private : 외부 접근 차단 - 이름 앞에 __(언더바 2개)를 붙이면 된다. 
'''

class Person:
    name = "유재석"        # 클래스 변수, public
    __addr = "대구시 중구"  # 클래스 변수, private

    def print_info(self):
        print(f"{self.name}님은 {self.__addr}에 거주합니다.")

    def __print_info(self): # private 메서드
        print(f"현재 {self.name}님은 {self.__addr}에 거주합니다.")

    def print_info2(self): # public 메서드
        print("print_info2")
        self.__print_info()
        
print(Person.name)
#print(Person.__addr)

yjs = Person()
yjs.print_info()

#yjs.__print_info()
yjs.print_info2()
