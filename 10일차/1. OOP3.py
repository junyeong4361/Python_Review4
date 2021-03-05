#OOP3.py

'''
    클래스 상속
        - 무언가를 물려 받는다.
        - 기존에 정의해놓은 클래스의 기능을 그대로 물려 받는 새로운 클래스를 정의한다.
        - 기반 클래스 : 부모클래스, 슈퍼클래스
        - 파생 클래스 : 자식클래스, 서브클래스

        - 자식클래스에서는 부모클래스의 변수, 메서드를 사용할 수 있다.

    [오버라이딩] - 재정의
        - 부모클래스에 정의된 메서드를 무시하고 자식클래스에서 같은 이름으로 다시 정의
        
'''

# 부모클래스
class person:
    def __init__(self, name, age):
        print("person, 생성자")
        self.name = name
        self.age = age
    def print_info(self):
        print("person, print_info")
        print("이름 :", self.name)
        print("나이 :", self.age)
    def sleep(self):
        print("person, sleep")
        print(self.name + "님은 8시간 잡니다.")

# 자식클래스
class student(person): # 상속받을 클래스를 ()안에 적는다.
    def __init__(self, name, age):
        print("student, 생성자!!!!")
        super().__init__(name, age)
        
    def study(self):
        print("student, study")
        print(self.name + "학생은 6시간 공부합니다.")

    def sleep(self):
        print("student, sleep")
        super().sleep()
        print(self.name + "학생은 7시간 잡니다.")


# 부모클래스의 인스턴스 생성
per = person("홍길동", 30)
per.print_info()
per.sleep()

# 자식클래스 인스턴스 생성
stu = student("아이유", 20)
stu.print_info()
stu.sleep() # 이름을 같게 만들면 부모의 것이 무시되고 자식의 것만 적용
stu.study()

# super().메서드명() -> 부모클래스의 메서드 호출



'''
        3. 책을 의미하는 Book 클래스
           전자책을 의미하는 EBook 클래스
        
            Book
                변수 : 제목, 정가
            EBook
                변수 : 보안키

    20000원짜리 "파이썬 최고" 책 1권
    15000원짜리 "파이썬 최고 - ebook" 전자책 1권 (보안키 1234)

            각각 인스턴스를 생성하여 정보 출력하기
            print_info()를 오버라이딩하고, super()를 활용하기

    [출력결과]
    이름 : 파이썬 최고
    가격 : 20000
    이름 : 파이썬 최고 - ebook
    가격 : 15000
    보안키 : 1234


'''
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print("이름 :", self.name)
        print("가격 :", self.price)

class EBook(Book):
    def __init__(self, name, price, key):
        super().__init__(name, price)
        self.key = key

    def print_info(self):
        super().print_info()
        print("보안키 :", self.key)

book = Book("파이썬 최고", 20000)
ebook = EBook("파이썬 최고 - ebook", 15000, "1234")
book.print_info()
ebook.print_info()






        
