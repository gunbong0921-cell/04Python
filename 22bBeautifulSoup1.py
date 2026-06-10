# 웹크롤링을 위해 2개의 모듈 임포트
import requests
from bs4 import BeautifulSoup

'''
네이버 지식in에서 검색어로 검색 후 인코딩 처리된 주소를 사용한다.
영문과 숫자를 제외한 모든 문자는 깨짐현상 방지를 위해 아래와 같이
인코딩되어 서버로 전송된다.
'''
url = 'https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
# requests 모듈을 통해 지식in 페이지의 HTML소스를 얻어온다.
response = requests.get(url)

# 응답코드가 200이면 정상적으로 접속된 상태로 판단
if response.status_code==200:
  # HTML 소스를 Text형식으로 변수에 저장
  html = response.text
  # 피싱을 위해 Soup객체로 변환. HTML이므로 html파서를 적용.
  soup = BeautifulSoup(html, 'html.parser')
  
  # 셀렉터로 추출(크롬) : 검색결과에서 첫번째 제목 추출
  title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt')
  # print("추출1_1:", title1_1)
  
  '''
  파이어폭스에서 복사한 Selector는 크롬과는 다를 수 있다. 하지만
  파싱한 결과는 동일하다.
  '''
  # 셀렉터로 추출(파이어폭스)
  # title1_2 = soup.select_one('.basic1 > li:nth-child(1) > dl:nth-child(1) > dt:nth-child(1) > a:nth-child(1)')
  # print("추출1_2:", title1_2)
  
  text = title1_1.get_text()
  # print("추출2:", text)
  
  '''
  검색결과 10갸를 포함하고 있는 <ul> 태그 하위의 <li> 태그를
  한꺼번에 얻어와서 파싱하기 위해 아래와 같이 선택자를 작성한다.
  ul태그중에 basic1이라는 클래스명을 가진 엘리먼트를 선택한다.
  '''
  ul = soup.select_one('ul.basic1')
  # 10개의 <li> 태그 전테가 출력된다.
  # print("추출3:", ul)
  
  # print("추출4")
  # 추출3에서 가져온 <ul>태그 하위에 반복되는 <li>를 얻어온다.
  titles2 = ul.select('li > dl > dt > a')
  # 그리고 검색결과의 갯수(10개)만큼 반복한다.
  for tit in titles2:
    # 모든 태그를 제거한 후 텍스트만 파싱해서 출력한다.
    print(tit.get_text())
else:
  print(response.status_code)    
  