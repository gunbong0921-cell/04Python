'''
예외처리
  : 에러를 핸들링하기 위해 사용된다.
  파이썬에서는 try~except를 사용한다. 그리고 else를 사용할 수 있다.
'''
def calc(val):
  sum = None
  try:
    # 0~2 인덱스 요소를 합산
    sum = val[0] + val[1] + val[2]
    if val[0]==100:
      # 정의됮 않은 변수를 출력하므로 에러
      print(no_var)
    elif val[0]==55:
      # 정수를 0으로 나누면 무한대가 되므로 에러
      result = val[0] / 0
      print("결과", result)
  # 예외명을 명시해서 특정 예외만 처리 
  except IndexError:
    print('리스트의 인덱스에 에러가 있습니다')
  # 예외발생시 에러메세지를 변수로 받은 후 출력 
  except NameError as err:
    print('선언되지 않은 변수를 사용하였습니다', str(err))
  # 예외명을 명시하지 않으면 모든 예외를 처리할 수 있다.  
  except:
    print('예외가 발생하였습니다')
  # 예외가 발생하지 않았을때 실행되는 블럭 
  else:
    print('에러없음^^')
  # 예외발생과 상관없이 무조건 실행되는 블럭 
  finally:
    print('sum', sum)
# 정상적으로 실행됨 
print('실행1')
calc([1, 2, 3])
# 요소가 2개밖에 없으므로 IndexError 발생
print('실행2')
calc([10, 20])
# 선언되지 않은 변수를 출력하므로 NameError 발생
print('실행3')
calc([100,101,102,102])
# ZeroDivisionError가 발생되어 except절에서 처리됨
print('실행4')
calc([55,56,57])
print('실행5')
'''
테스트시 2단계로 나눠서 확인해본다.
Step1 : 최초 실행시에는 애국가 파일이 없는 상태이므로 IOError 발생
Step2 : 애국가 파일을 직접 생성한 후 실행하면 파일의 끝까지
    내용을 읽은 후 예외가 발생된다.
'''
try:
  fp = open('./saveFiles/애국가.txt', mode="rt", encoding='utf-8')
  try:
    while True:
      lines = fp.readlines()
      if not lines: break
      print(lines)
  finally:
    print("예외]더 이상 읽을 내용이 없습니다")
    fp.close()
except IOError:
  print('예외]파일이 없습니다')     
                     