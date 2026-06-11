import requests
from bs4 import BeautifulSoup

# KBO 타자 기록실
response = requests.get("https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT")
# HTNL 소스 저장(텍스트 형식)
html = response.text
# 파싱을 위해 Soup 객체로 변환
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 타이틀 파싱 : 선수기록(HTML태그 포함)
title = soup.select_one('#contents > div.sub-content > div.tab-depth2 > ul > li.on > a')
print("title 요소 :", title)
# 태그를 제거한 후 순수한 텍스트만 추출

title_txt = title.get_text()
print("title 텍스트 :", title_txt)

# 타자 기록이 있는 <table> 태그 전체 얻어오기
record_table = soup.select_one("#cphContents_cphContents_cphContents_udpContent > div.record_result > table")
# print("타자기록 요소 :", record_table)

# 타자 기록이 반복 출력되는 <tbody>를 얻어온 후 <tr>의 갯수만큼 반복
record_tr = soup.select_one("#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody")
# select() 함수는 반복되는 요소를 List로 얻어온다.
repeat_tr = record_tr.select('tr')
for rec in repeat_tr :
  # print("dddd", rec)
  
  d1 = rec.select_one('td:nth-child(1)').get_text() # 순위
  d2 = rec.select_one('td:nth-child(2)').get_text() # 선수명
  d3 = rec.select_one('td:nth-child(3)').get_text() # 팀명
  d4 = rec.select_one('td:nth-child(4)').get_text() # 타율
  d5 = rec.select_one('td:nth-child(5)').get_text() # 경기
  d6 = rec.select_one('td:nth-child(6)').get_text() # 타석
  d7 = rec.select_one('td:nth-child(7)').get_text() # 타수
  d8 = rec.select_one('td:nth-child(8)').get_text() # 안타
  d9 = rec.select_one('td:nth-child(9)').get_text() # 2루타
  d10 = rec.select_one('td:nth-child(10)').get_text() # 3루타
  d11 = rec.select_one('td:nth-child(11)').get_text() # 홈런
  d12 = rec.select_one('td:nth-child(12)').get_text() # 타점
  d13 = rec.select_one('td:nth-child(13)').get_text() # 도루
  d14 = rec.select_one('td:nth-child(14)').get_text() # 도루실패
  d15 = rec.select_one('td:nth-child(15)').get_text() # 볼넷
  d16 = rec.select_one('td:nth-child(16)').get_text() # 사구
  d17 = rec.select_one('td:nth-child(17)').get_text() # 삼진
  d18 = rec.select_one('td:nth-child(18)').get_text() # 병살타
  d19 = rec.select_one('td:nth-child(19)').get_text() # 실책                                  

  # 출력(행 들여쓰기 해야 전체출력됨)
  print(d1, d2, d3, d4, d5, d6, d7, d8, d9 ,d10, d11, d12, d13, d14, d15, d16, d17, d18, d19) 
  # DB입력


