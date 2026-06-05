'''
break : 반복문을 즉시 탈출
continue : 반복문의 처음으로 돌아가서 조건 확인
'''

repeat = 0
while True:
  repeat += 1
  num = int(input('숫자하나를 입력하세요:'))
  if num%2 == 0:
    print(f'입력한 {num}은 2의 배수이므로 계속합니다.')
    continue
  elif num%7 == 0:
    print(f'입력한 {num}은 7의 배수이므로 탈출합니다.')
    break
  else:
    print("2와 7의 배수가 아니면 계속합니다.")
print(f'전체반복횟수 : {repeat}')    