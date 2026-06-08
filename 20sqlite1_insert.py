# SQLite 모듈은 기본으로 제공되므로 import만 하면 사용가능
import sqlite3
import random

# sqlite 연결 및 DB파일 생성
conn = sqlite3.connect('./saveFiles/biography.db')
# 커서 생성. 이 객체를 통해 여러가지 DB작업을 할 수 있다.
curs = conn.cursor()
# 입력값 구분을 위해 난수 생성
rnd = random.randint(0,100);

# 테이블생성.
try:
  '''
  테이블이 없는 최초 실행이라면 새롭게 생성된다. 컬럼의 자료형은
  파이썬의 자료형을 사용했는데, SQLite의 자료형을 사용해도 된다.
  '''
  tb1cmd = 'create table people (name char, job char, pay int)'
  # 쿼리문의 실행은 커서를 이용한다.
  curs.execute(tb1cmd)
except Exception as e:
  '''
  2번째 실행에서 테이블이 이미 생성된 상태라면 예외가 발생하게
  되므로 except 절에서 처리해야한다. 혹은 쿼리문에 if not exist
  를 추가해도 된다.
  '''
  print("[예외발생]테이블은 이미 생성되었습니다.", e)
  
# 레코드 1개 삽입. 튜플을 사용해서 인파라미터를 설정
curs.execute('insert into people values (?,?,?)', (f'이순신{rnd}','장군',500))

'''
레코드 2개 이상 삽입, 튜플로 구성된 리스트 사용함.
이때는 executemany() 함수를 사용한다.
'''
curs.executemany('insert into people values (?,?,?)', 
                 [(f'강감찬{rnd}','장군',700), [f'홍길동{rnd}','의적',800]])

# 반복문(for문)을 통해 여러개의 데이터 삽입
rows = [[f'곽재우{rnd}','의병',1100], [f'유성룡{rnd}','재상',1200],
        [f'임꺽정{rnd}','의적',1500]]
# 입력데이터로 사용할 리스트의 크기만큼 반복해서 쿼리문을 실행한다.
for row in rows :
  curs.execute('insert into people values (?,?,?)', row)
# 입력을 마쳤다면 커밋 
conn.commit()
print('레코드 insert 및 commit 완료')   