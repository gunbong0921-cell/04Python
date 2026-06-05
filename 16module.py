'''
모듈 : 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든
  파일로 변수 혹은 함수 등을 모아놓은것을 말한다.
'''

'''
방법1 : 모듈명만 임포트한다. 이 경우 모듈명을 함께 작성해서
  함수를 호출한다.
'''
import mod1
print("모듈의 함수호출1 :", mod1.add(3, 4))
print("모듈의 함수호출2 :", mod1.add(4, 2))

# 방법2 : 모듈내에 정의된 특정 함수만 임포트
from mod1 import add
# 이 경우에는 모듈명을 생략한 상태로 호출할 수 있다.
result = add(3, 4)
print("결과 :", result)

# 방법3 : 방법2와 동일하지만 모든 함수를 한꺼번에 임포트하는 방식
from mod1 import *
result1 = add(3, 4)
print("결과 :", result1)
result2 = sub(3, 4)
print("결과 :", result2)

# __name__ 변수를 사용하여 작성된 모듈 임포트
import mod2
# 임포트하면 __name__에는 'mod2'가 저장되므로 if문은 실행되지않음.
result = mod2.mul(3, 4)
print(result)

# 모듈을 용도별로 나누어 관리할때는 패키지(폴더)를 사용한다.
import commons.mod3
# 패키지명까지 포함한 형태로 함수 호출
commons.mod3.sum1To10()

# 함수명 만으로 호출
from commons.mod3 import sum1To10
sum1To10()