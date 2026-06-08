import sqlite3

# DB연결 및 커서 생성
conn = sqlite3.connect('./saveFiles/biography.db')
curs = conn.cursor()

# 조회된 레코드를 한꺼번에 출력하기(리스트 형식으로 출력됨)
print(f"{'조회1':-^30}")
curs.execute('select * from people')
print(curs.fetchall())

# 조회된 결과를 한 행(Row)씩 출력
print(f"{'조회2':-^30}")
curs.execute('select * from people')
for row in curs.fetchall():
  print(row)
  
# 각 컬럼별로 출력
print(f"{'조회3':-^30}")
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
  print(name, ':', job, ':', pay)
  
  print("전체 레코드 select 완료")