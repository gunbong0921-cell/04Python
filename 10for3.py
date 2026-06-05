'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년츄가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''

# 숫자형으로 연/월/일을 입력받는다.
year = int(input("년도를 입력하시오:"))
month = int(input("월을 입력하시오:"))
day = int(input("일을 입력하시오:"))

# 서기 1년1월1일(월요일)부터 입력한 날짜까지의 일수를 누적
total_days = 0

'''
월별 날짜수를 리스트로 정의. 1월을 인덱스 1로 사용하기 위해
첫번째 요소는 0으로 설정한다.
'''
year_month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

'''
입력한 이전년도(작년)까지의 전체 날짜를 누적해서 더해준다
'''
for d in range(1,year):
  if d % 400 == 0: # 400으로 나눠지면 윤년
    total_days = total_days + 366
  elif d % 100 == 0: # 100으로 나눠지면 평년
    total_days = total_days + 365
  elif d % 4 == 0: # 4로 나눠지면 윤년
    total_days = total_days + 366
  else: # 그 외는 모두 평년이므로 365일로 계산
    total_days = total_days + 365

'''
입력 년도의 각 월의 날짜수를 누적해서 합산한다. 만약 1월을
입력했다면 이 for문은 실행되지 않는다.
'''    
for m in range(1, month):
  total_days = total_days + year_month_days[m]

'''
입력월이 3 이상이고, 입력년도가 윤년인 경우 1을 더해줘야한다.
윤년은 2월 29일까지 있기 때문이다. 만약 1월 혹은 2월을 입력했다면
이 부분은 고려할 필요가 없다.
'''  
if month >= 3:
  if year % 400 == 0:
    total_days = total_days + 1
  elif year % 100 == 0:
    total_days = total_days + 0
  elif year % 4 == 0:
    total_days = total_days + 1
  else:
    total_days = total_days + 0

# 마지막으로 내가 입력한 날짜를 합산 
total_days += day
print()
# 누적된 날짜 확인
print("total_days :", total_days)
'''
서기 1년1월1일은 월요일이므로 7로 나눈 나머지를 통해 요일을 판단할
수 있다. 나누어 떨어지면 일요일, 1이 남으면 월요일로 판단한다.
'''
remainder = total_days % 7

if remainder == 0:
  print("일요일입니다.")   
if remainder == 1:
  print("월요일입니다.")    
if remainder == 2:
  print("화요일입니다.")    
if remainder == 3:
  print("수요일입니다.")    
if remainder == 4:
  print("목요일입니다.")    
if remainder == 5:
  print("금요일입니다.")    
if remainder == 6:
  print("토요일입니다.")                                

'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''
print("--- 요일 계산 프로그램 ---")
year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

# 1. 서기 1년부터 입력한 년도의 전년도까지의 총 일수 계산 (윤년 규칙 반영)
total_days = (year - 1) * 365 \
             + (year - 1) // 4 \
             - (year - 1) // 100 \
             + (year - 1) // 400

# 2. 각 달의 일수 설정 (인덱스와 월을 맞추기 위해 앞에 0 추가)
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 입력받은 올해가 윤년인지 확인하여 2월을 29일로 변경
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    month_days[2] = 29

# 1월부터 이전 달까지의 일수를 모두 더함
total_days += sum(month_days[:month])

# 3. 입력받은 '일'만큼 총 일수에 더하기
total_days += day

# 4. 요일 판별 (서기 1년 1월 1일은 월요일 -> 나머지가 1이면 월요일)
# 나머지가 0=일요일, 1=월요일, 2=화요일, 3=수요일, 4=목요일, 5=금요일, 6=토요일
day_of_week = ["일", "월", "화", "수", "목", "금", "토"]
result_index = total_days % 7

print("\n--- 결과 ---")
print(f"{year}년 {month}월 {day}일은 [{day_of_week[result_index]}요일] 입니다.")