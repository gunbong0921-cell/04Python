import sqlite3

conn = sqlite3.connect('./saveFiles/biography.db')
curs = conn.cursor()

# 조회1
print(f"{'조회1':-^30}")
curs.execute('select * from people')
print(curs.fetchall())

# 조회2
print(f"{'조회2':-^30}")
curs.execute('select * from people')
for row in curs.fetchall():
  print(row)
  
# 조회3
print(f"{'조회3':-^30}")
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
  print(name, ':', job, ':', pay)
  
  print("전체 레코드 select 완료")