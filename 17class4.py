'''
클래스변수와 정적메서드
  : 클래스를 통해 생성되는 인스턴스에는 멤버변수와 멤버함수가
  포함된다. 하지만 클래스변수와 정적메서드는 인스턴스 내부에 존재
  하지 않고 별도의 메모리에 독립적으로 생성된다. 따라서 2개 이상의
  인스턴스를 생성해도 딱 하나만 생성되어 모든 인스턴스가 공유하게
  된다.
'''
class MyCalculator:
  '''
  클래스 변수(정적변수) : 클래스 전체에서 공유되는 변수로 메모리에 딱 하나만 생성됨.
  '''
  calCount = 0
  # 생성자
  def __init__(self, first, second):
    # 멤버(인스턴스)변수 : 생성된 인스턴스마다 존재함.
    self.first = first
    self.second = second
  # 멤버함수(인스턴스함수) 
  def calculate(self, symbol):
    # 클래스명을 통해 정적변수에 접근하여 1씩 증가시킴.
    MyCalculator.calCount += 1
    # 멤버변수는 self를 통해 접근한 후 사칙연산을 수행
    if symbol == "+":
      result = self.first + self.second
    elif symbol == "-":
      result = self.first - self.second
    elif symbol == "*":
      result = self.first * self.second
    elif symbol == "/":
      result = self.first / self.second
    # 계산 결과 반환 
    return result
  
  # 정적메서드 정의. 데코레이터를 사용한다.
  @staticmethod
  def otherNumMulti(refCls, otherNum):
    '''
    해당 함수는 정적함수로 정의되었으므로 인스턴스 외부에
    독립적으로 생성된다. 따라서 특정 인스턴스의 멤버변수에
    접근하기 위해 인스턴스의 참조값을 매개변수로 받은 후
    사용해야한다.
    '''
    result = (refCls.first + refCls.second) * otherNum
    # 계산횟수 증가
    MyCalculator.calCount += 1
    # 콘솔에 결과와 계산횟수 출력
    print("결과: ", result)
    print("연산횟수: ", MyCalculator.calCount)
  # 참조변수 자체를 출력할때 사용되는 함수 
  def __str__(self):
    str = f'계산기 클래스 입니다.' \
      f'first={self.first}, second={self.second}'  
    return str
  
# 인스턴스 생성
cal1 = MyCalculator(5, 9)
cal2 = MyCalculator(3, 4)

# 인스턴스1을 통한 연산
print('덧셈(cal1): ', cal1.calculate('+'))
print('곱셈(cal1): ', cal1.calculate('*'))

# 인스턴스2를 통한 연산
print('뺄셈(cal2): ', cal2.calculate('-'))
print('나눗셈(cal2): ', cal2.calculate('/'))

# 클래스 변수는 딱 하나만 생성되므로 전체 계산횟수 4개만 출력된다.
print('계산횟수: ', MyCalculator.calCount)

'''
정적함수는 참조변수가 아니라 클래스명으로 직접 호출한다. 즉 함수
호출을 위해 인스턴스를 생성할 필요가 없다.
단 정적함수 내부에서 특정 인스턴스의 멤버변수에 접근하기 위해서는
참조변수가 필요하므로 인수로 전달해준다.
'''
MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)

# 인스턴스메서드는 클래스명으로 호출 불가 (예외 에러 발생하므로 주석 처리)
# MyCalculator.calculate('/')
  