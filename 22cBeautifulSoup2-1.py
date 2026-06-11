import pymysql
import requests
from bs4 import BeautifulSoup

# 1. KBO 타자 기록실 웹 크롤링
response = requests.get("https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

title = soup.select_one('#contents > div.sub-content > div.tab-depth2 > ul > li.on > a')
title_txt = title.get_text() if title else "타자기록"
print("타이틀 :", title_txt)

# 2. MariaDB 연결 설정 (본인의 DB 정보로 수정 필요)
conn = pymysql.connect(
    host='localhost',          # DB 서버 주소 (예: '127.0.0.1' 또는 외부 IP)
    user='sample_user',               # DB 사용자 이름
    password='1234',  # DB 비밀번호 (꼭 변경하세요!)
    database='sample_db',      # 사용할 데이터베이스 명
    charset='utf8mb4'
)
cursor = conn.cursor()

# 테이블 생성 (MariaDB 문법)
cursor.execute('''
CREATE TABLE IF NOT EXISTS hitter_records (
    `rank` INT,
    `name` VARCHAR(50),
    `team` VARCHAR(50),
    `avg` DOUBLE,
    `g` INT,
    `pa` INT,
    `ab` INT,
    `h` INT,
    `2b` INT,
    `3b` INT,
    `hr` INT,
    `rbi` INT,
    `sb` INT,
    `cs` INT,
    `bb` INT,
    `hbp` INT,
    `so` INT,
    `gdp` INT,
    `e` INT
)
''')

# 기존 데이터 비우기 (TRUNCATE가 DELETE보다 대용량 처리 시 빠릅니다)
cursor.execute('TRUNCATE TABLE hitter_records')

# 3. 데이터 파싱 및 수집
record_tr = soup.select_one("#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody")
repeat_tr = record_tr.select('tr')

data_to_insert = []

for rec in repeat_tr:
    row_data = [td.get_text().strip() for td in rec.select('td')]
    
    if len(row_data) == 19:
        try:
            # 데이터 타입 변환 및 저장 리스트 추가
            formatted_row = (
                int(row_data[0]),      # 순위
                row_data[1],           # 선수명
                row_data[2],           # 팀명
                float(row_data[3]),    # 타율
                int(row_data[4]),      # 경기
                int(row_data[5]),      # 타석
                int(row_data[6]),      # 타수
                int(row_data[7]),      # 안타
                int(row_data[8]),      # 2루타
                int(row_data[9]),      # 3루타
                int(row_data[10]),     # 홈런
                int(row_data[11]),     # 타점
                int(row_data[12]),     # 도루
                int(row_data[13]),     # 도루실패
                int(row_data[14]),     # 볼넷
                int(row_data[15]),     # 사구
                int(row_data[16]),     # 삼진
                int(row_data[17]),     # 병살타
                int(row_data[18])      # 실책
            )
            data_to_insert.append(formatted_row)
        except ValueError:
            continue

# 4. DB에 대량 삽입 (MariaDB는 플레이스홀더로 %s를 사용합니다)
insert_query = '''
INSERT INTO hitter_records 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
cursor.executemany(insert_query, data_to_insert)
conn.commit()

print(f"성공적으로 {len(data_to_insert)}건의 데이터가 MariaDB 'sample_db'에 저장되었습니다.")

# 5. 확인 출력
cursor.execute("SELECT * FROM hitter_records LIMIT 5")
print("\n--- MariaDB 저장 데이터 상위 5건 확인 ---")
for row in cursor.fetchall():
    print(row)

# 연결 종료
cursor.close()
conn.close()