'''
파이썬에서 MySQL(MariaDB)를 연동하려면 PyMySQL을 먼저 설치해야
한다.
C:\> pip install pymysql
'''
# 모듈 임포트
import pymysql

# DB연결(호스트, DB명, 사용자계정, 패스워드 등이 필요함)
conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
          database='sample_db', charset='utf8', port=3306)
'''
port의 경우 기본포트인 3306을 사용중이라면 생략할 수 있다. 만약 포트가 틀린 경우라면
추가해야한다.

cursorclass=pymysql.cursors.DictCursor
  : 이 옵션을 사용하면 레코드 인출시 딕셔너리로 출력된다.
  생략시 디폴트값은 튜플로 설정되어 있다.
''' 
# 커서 생성
curs = conn.cursor()
# SQL 작업을 위해서는 반드시 try~except로 예외처리 해야한다.
try:
  # 쿼리문 작성 및 실행
  sql = "SELECT * FROM board"
  curs.execute(sql)
  
  # select한 모든 레코드 인출
  rows = curs.fetchall()
  print('단순인출', rows)
  
  print(f"{'인출1':-^30}")
  # 행 단위로 하나씩 인출하여 출력
  for row in rows:
    print(row)
    
  print(f"{'인출2':-^30}")
  # 행 단위로 인출하되 각 칼럼의 인덱스를 지정하여 개별 인출
  for row in rows:
    # 인덱스 0은 num. 이후는 순서대로 지정된다.
    print(row[0], row[1], row[2], end=" ")
    pdate = row[3]
    id = row[4]
    vcnt = row[5]
    # 변수에 저장한 후 서식문자를 이용해서 출력
    print("%s, %s, %s" % (pdate, id, vcnt))
    
  print(f"{'인출3':-^30}")
  # 검색어와 like를 이용해서 검색 결과 인출
  sql = sql + " WHERE title like '%{0}%' ".format(input ('검색어입력:'))
  curs.execute(sql)
  rows = curs.fetchall()
  print(rows)
except Exception as e:
  print("쿼리 실행시 오류발생", e)
  
print('-'*40)
conn.close()
print('자원반납')
        