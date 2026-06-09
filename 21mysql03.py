import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
          database='sample_db', charset='utf8', port=3306)
curs = conn.cursor()

# format() 함수는 인덱스를 통해 값을 설정할 수 있다.
sql = """update board
          set title='{1}', content='{2}'
          where num={0}""".format(input('수정할일련번호:'), input('제목:'), input('내용:'))
          
try:
  curs.execute(sql)
  conn.commit()
  print("1개의 레코드가 수정됨")
except Exception as e:
  conn.rollback()
  print("쿼리 실행시 오류발생", e)
  
conn.close()
              