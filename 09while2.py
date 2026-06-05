'''
시나리오]1부터 20까지의 숫자 중 홀수만 출력하는 프로그램을 작성하시오.
    단 continue를 사용하시오.
'''
a = 1
while a <= 20:
  if a % 2 == 0:
    # i가 짝수인 경우 단순히 1증가
    a = a + 1
    # 반복문 안에서 만나면 처음으로 돌아간다.
    continue
  else:
    # 홀수인 경우에는 줄바꿈없이 출력
    print(a, end=' ')
    a += 1
    
print()
print("="*30)

# 시나리오] 구구단을 출력하시오.
dan = 2
# 단에 해당하는 반복문(외부)
while dan<=9 :
  su = 1
  # 수에 해당하는 반복문(내부)
  while su<=9:
    # 서식 문자를 이용한 구구단 출력.
    # %2d : 2칸을 확보한 후 문자열 출력. 
    print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
    su += 1
  dan += 1
  # 하나의 단을 출력한 후 줄바꿈
  print()
    
print()
print("="*30)

# 시나리오] 구구단을 출력하되 짝수단만 출력하시오.
dan = 2
while dan<=9 :
  if dan%2 == 1: 
    # 단이 홀수이면 while문의 터음으로 돌아감
    # 다음 단 출력을 위해 1 증가
    dan += 1
    continue
  else: 
    # 단이 짝수일때만 구구단 출력
    su = 1
    while su<=9:
      # print()문을 서식에 맞춰서 사용하는 형태
      print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
      su += 1
  dan += 1
  print()
print()        