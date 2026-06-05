'''
시나리오]1~100사이의 정수 중 3의 배수의 합을 구하시오.
'''
total = 0
# 1~100까지 반복(미만이므로 1개 더표시해야함)
for i in range(1, 101):
  # 3의 배수 확인
  if i % 3 ==0:
    # 누적해서 합산
    total += i 
    # 3의 배수를 줄바꿈 없이 +로 연결해서 출력
    print(i, end='+')
print('\b', '=', total)

print()
print("="*30)

'''
List Comprehension
  : 대괄호 안에 for문으로 반복적인 표현식을 실행해서 리스트의
  요소를 초기화하는 방법
  형식]
    [ 표현식 for 요소 in 컬렉션 [if조건식] ]
    for문의 반복 횟수만큼 표현식을 실행해서 리스트를 채워준다.
    단, if조건식은 생략할 수 있다.
'''
# 0~9까지의 정수중 3의 배수의 제곱으로 구성된 리스트를 생성
list = [n ** 2   for n in range(10)   if n%3==0]
print(list) # [0, 9, 36, 81]
#  if n%3==0 삭제 시 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()
print("="*30)

'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''
# 4행4열인 매트릭스 출력 
for x in range(1,5):
    for y in range(1,5):
        # 행과 열이 동일할때 1 출력. 줄바꿈없이 공백으로 구분. 
        if x == y:
            print("1", end=' ')
        else:
            # 값이 서로 다를때는 0 출력. 
            print("0", end=' ')
    # 한 행을 모두 출력하면 줄바꿈 처리 
    print()

# matrix = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
# for row in matrix:
#   print(*(row))
    
print()    
print("="*30)

'''
퀴즈] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

*
**
***
****
*****
'''
# 0~4까지 5번 반복 
for i in range(5): # 행 
    for j in range(5): # 열 
        # i가 늘어나는 만큼 j가 반복되는 조건  
        if i >= j:
            print("*", end=" ")     
    # 한 행이 출력되면 줄바꿈
    print() 

# for i in range(1, 6):
#   print("*" * i)
  
print()
print("="*30)
              