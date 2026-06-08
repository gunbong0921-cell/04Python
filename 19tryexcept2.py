# 개발자가 직접 예외 발생시키기
print('실행6')
try:
  x = int(input('3의 배수를 입력하세요: '))
  # 사용자가 입력한 숫자가 3의배수가 아닌 경우 예외를 발생시킴
  if x % 3 != 0:
    # 파이썬에서는 raise를 사용한다.(Java의 throw와 동일)
    raise Exception('[예외메세지] 3의 배수가 아님')
  print(x)
except Exception as e:
  print('예외가 발생했습니다.', e)

'''
개발자가 정의하는 예외클래스
  : 예외클래스 정의시 Exception 클래스를 상속하고, 생성자에서
  예외 발생시 출력할 에러 메세지를 정의한다.
'''  
print('실행7')
# 파이썬에서는 상속시 extends를 사용하지 않고, 매개변수 형태로 상속을 구현한다.
class GugudanRangeExcept(Exception):
  # 생성자
  def __init__(self):
    # 부모클래스인 Exception 클래스의 생성자 호출
      super().__init__('구구단의 범위를 벗어났습니다')

# 매개변수로 전달된 숫자만큼의 구구단을 출력하는 함수 정의
def print_gugudan(end_num):
  try:
    if end_num > 9:
      # 9를 초과하는 경우 졍의한 클래스를 이용해서 예외를 발생시킴
      raise GugudanRangeExcept
    # range()는 항상 미만까지만 반복하므로 1을 더해준다.
    end_su = end_num + 1
    for dan in range(2,end_su):
      for su in range(1, 10):
        # 하나의 단을 줄바꿈없이 출력
        print("%d * %d = %2d" % (dan, su, dan*su), end=' ')
      # 단이 완료되면 줄바꿈 처리 
      print()
    print()
  except Exception as e:
    print('예외발생', e)
    
print_gugudan(int(input("출력할 단 수를 입력하세요:")))                
      
          