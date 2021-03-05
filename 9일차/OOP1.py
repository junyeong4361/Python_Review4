# OOP1.py

'''
    [Object Oriented Programming]
        - 객체지향 프로그래밍

        1. 클래스는 속성(변수)을 정의하거나, 기능(함수)을 정의할 수 있다.
            > 함수와 마찬가지로 클래스도 작성해놓기만 하면 프로그램 수행에 영향이 없다.
            > 객체를 생성한 뒤부터 클래스에 작성된 코드가 효력이 발생한다.

        2. 클래스 안에 정의된 함수를 '메서드'라고 부른다.
            > 메서드를 만들 때는 반드시 최소 하나의 매개변수가 필요하다.
            > 나 자기 자신을 의미하는 self라는 이름으로 한다.
                >> self는 매개변수가 아니라 인스턴스(객체명)

'''
# 클래스 만들기

# class 클래스명:
#     변수명
#     def 함수명(self):
#         수행문

class Car:
    def power_on(self):
        print("부릉부릉!")
        self.power = True
        self.drive()

    def drive(self):
        print("주행시작!")

# 인스턴스 생성 -> 인스턴스명 = 클래스명()
bmw = Car()
# 전에는 이렇게 사용했다면  "문자열".함수(),   리스트.함수()

# 인스턴스명.함수명()
bmw.power_on()
print("bmw의 시동 여부 :", bmw.power)

# 클래스에 여러 속성/기능을 정의 해두고, 인스턴스라는 하나의 단위로 묶어서 다루겠다.

tico = Car()
sonata = Car()

tico.drive()
tico.power = "시동 켜짐"
print("tico의 시동 여부 :", tico.power)
tico.model = "최신 모델!"
print(tico.model)
print()
# 만들어지는 인스턴스별로 속성(변수)이 다를 수 있다. 

# 1. 클래스를 왜 사용할까?

# 클래스 없이 자동차 2대를 다뤄보기
car1_model = "BMW"
car1_power = False
car1_max_speed = 200

car2_model = "SONATA"
car2_power = True
car2_max_speed = 180

def drive_car(model, power, max_speed, speed): # speed : 내가 주행하고 싶은 속도 
    print(f"{model} 주행 준비...")
    if power == False:
        print("주행불가 : 시동을 켜주세요.")
        return
    if speed > max_speed:
        print(f"{model}의 최고속도는 {max_speed}입니다. 속도를 줄입니다.")
        speed = max_speed
    print(f"{speed}km로 주행합니다. 출발~~")
drive_car(car1_model, car1_power, car1_max_speed, 200)
drive_car(car2_model, car2_power, car2_max_speed, 200)
# 각 변수들은 서로 전혀 연관성이 없다.
# 함수를 호출할 때 일일이 매개변수로 모든 값을 전달해야 한다.
print()

# 2. 클래스의 사용 1
class Car:
    def drive_car(self, speed):
        print(f"{self.model} 주행준비...")

        if self.power == False:
            print("주행불가 : 시동을 켜주세요.")
            return
        if speed > self.max_speed:
            print(f"{self.model}의 최고 속도는 {self.max_speed}입니다. 속도를 줄입니다.")
            speed = self.max_speed
        print(f"{speed}km로 주행합니다. 출발~~")
car1 = Car()
car2 = Car()

car1.model = "BMW"
car1.power = False
car1.max_speed = 200

car2.model = "SONATA"
car2.power = True
car2.max_speed = 180

car1.drive_car(200)
car2.drive_car(200)

# drive_car 호출 시, 정의된 매개변수는 2개이다. (self, speed)
# self에는 자동으로 호출하는 인스턴스가 대입
# 그 뒤 매개변수부터는 호출할 때 값을 전달해야 한다.

# 함수를 호출할 때 그냥 호출해도 self에는 인스턴스가 대입되기 때문에
# 함수의 수행문 안에서 밖에서 만든 속성들을 그대로 사용할 수 있다.

print()

# 3. 생성자
#   > 인스턴스 생성 시 자동으로 호출되는 메서드(함수) -- 무조건 호출된다.
#   > 목적 : 인스턴스 생성과 동시에 속성을 추가/초기값 지정하고 싶을 때 사용 (초기화)
#   > 생성자 함수의 이름 : __init__(언더바 2개씩)

class Car:
    def __init__(self, m, p, ms):
        print("생성자 호출!")
        self.model = m
        self.power = p
        self.max_speed = ms
        
    def drive_car(self):
        print(self.model + "주행 시작!")

car1 = Car("BMW", False, 200) # 생성자함수를 호출하는 코드
print("car1의 모델 :", car1.model)
car1.drive_car()
print()

# 4. 생성자를 활용

class Car:
    def __init__(self, m, p, ms):
        print(f"[{m}] 인스턴스 생성!")
        self.model = m
        self.power = p
        self.max_speed = ms

    def drive_car(self, speed):
        print(f"{self.model} 주행 준비...")

        if self.power == False:
            print("주행불가 : 시동을 켜주세요.")
            return
        if speed > self.max_speed:
            print(f"{self.model}의 최고 속도는 {self.max_speed}입니다. 속도를 줄입니다.")
            speed = self.max_speed
        print(f"{speed}km로 주행합니다. 출발~~")

        
car1 = Car("BMW", False, 200)
car2 = Car("SONATA", True, 180)
car1.drive_car(200)
car2.drive_car(200)

