# 클래스 연습하기
'''
    1. 학생 클래스 만들기 (Student)
        속성(변수) : 이름(name), 나이(age), 전화번호(phone), 과목(sub)
        기능(함수)
            1. 생성자 __init__
                > 매개변수로 이름,나이,전화번호,과목을 전달 받고, 각 속성 생성 및 대입
            2. 정보 출력 (print_info)
                > 객체에 만들어져 있는 이름,나이,전화번호 를 출력
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-5678
            3. 공부하기 (study)
                > 객체에 만들어져 있는 이름,과목 출력
                    홍길동 님이 파이썬 공부를 시작합니다.

        - 학생 3명 만들어서 '정보출력', '공부하기' 메서드를 호출해서 출력 결과 확인
            hong.print_info() <-- 이런거 하자는 얘기
'''

class Student:
    def __init__(self, name, age, phone, sub):
        self.name = name
        self.age = age
        self.phone = phone
        self.sub = sub

    def print_info(self):
        print("이름 :", self.name)
        print("나이 : {}세".format(self.age))
        print("전화번호 :", self.phone)

    def study(self):
        print(f"{self.name} 님이 {self.sub} 공부를 시작합니다.")

iu = Student("아이유", 20, "010-1111-2222", "파이썬")
yjs = Student("유재석", 33, "010-2222-3333", "C언어")
kjk = Student("김종국", 40, "010-2345-6789", "JAVA")

iu.print_info()
yjs.print_info()
kjk.print_info()

iu.study()
yjs.study()
kjk.study()

