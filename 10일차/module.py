# module.py

'''
    모듈
        - 변수, 함수, 클래스 등을 모아 놓은 소스 파일
        - 간단한 기능을 담을 때 사용
        - 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만들어진 소스 파일

        sys.path 안에 모듈이 위치해 있어야 한다.
        
'''
'''
import sys
print(sys.path)
# sys.path.append("C:\\test\\abc") 형태로 추가 가능
print()
'''

# 모듈 불러오기 (1) - 모듈명 그대로 사용
'''
import koreais_module
print(koreais_module.str1)
print(koreais_module.add(1, 2))
print(koreais_module.mul(2, 4))
dog = koreais_module.Dog("바둑이")
dog.cry()

import random
print(random.randint(1, 3))
'''

# 모듈 불러오기 (2) - as 별칭 주기
'''
import koreais_module as km
print(km.str1)
print(km.add(2, 4))
print(km.mul(3, 5))
dog = km.Dog("초코")
dog.cry()
#print(koreais_module.str1)

import random as r
print(r.randint(1, 3))
'''

# 모듈 불러오기 (3) - 모듈에서 일부만 사용
"""
from koreais_module import str1, add, Dog
# 변수명, 함수명, 클래스명만 사용
# from으로 import하면 모듈명은 생략
print(str1)
print(add(4, 5))
dog = Dog("바둑이")
dog.cry()
#print(mul(2, 3)) # 가져오지 않은 함수 -> 오류
#print(koreais_module.str1) # 모듈명 포함하면 오류
"""

# 모듈 불러오기 (4) - 모듈에서 전체를 사용
'''
from koreais_module import *
print(str1)
print(add(1, 3))
print(mul(2, 3))
dog = Dog("바둑이")
dog.cry()
'''
# 모듈을 import를 할 때, 모듈명을 생략하는
# 3, 4번 방식은 좋지 않다.
# 모듈을 여러 개 import하다보면
# 각 모듈에서 이름이 겹칠 수 있다.
# 가장 좋은 방법은 2번 별칭주기


import koreais_module

# 파이썬 프로그램을 실행 하는 주체
#   > 실행을 하는 소스파일이 main이 된다.
# import에 의해 실행되는 소스 파일은 '모듈'






























































































