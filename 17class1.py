# 클래스 정의
class Person:
  # 생성자 함수. 첫번째 매개변수로 자신을 가리키는 self 사용.
  def __init__(self, name, age):
    # 멤버변수 선언 및 초기화
    self.name = name
    self.age = age
  # 멤버 함수 정의 
  def showInfo(self):
    # 멤버변수 출력용으로 정의
    print(f"이름 : {self.name}")
    print(f"나이 : {self.age}")
  def justDoIt(self, act):
  # 멤버변수와 매개변수를 동시에 출력하는 용도로 정의 
    print(f"{self.name} 님이 {act} 을(를) 합니다.")
    '''
    Java의 toString()과 동일한 역활의 함수로 인스턴스 변수를
    그대로 출력할때 문자열로 반환해준다.
    '''    
  def __str__(self):
    return f"제 이름은 {self.name}({self.age})입니다."

# 인스턴스 생성. Java와 같이 new 연산자 없이 클래스 이름과 매개변수로 생성자를 호출한다. 
person1 = Person("박찬호", 30)
person2 = Person("손흥민", 28)

# 인스턴스 변수를 통해 멤버함수 호출
person1.showInfo()
person1.justDoIt("야구")

'''
toString()의 역할을 하는 __str__()를 통해 반환된 문자열이
출력된다. 이 함수를 정의하지 않으면 인스턴스 참조값이 출력된다.
'''
print(person2)
person2.justDoIt("축구")