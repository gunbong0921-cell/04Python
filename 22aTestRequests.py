import requests
response1 = requests.get('https://www.naver.com/')
# print(response1.status_code) # 응답코드를 출력
# print(response1.text) # HTML 코드를 출력

# 네이버 블로그 통합페이지에서 사용하는 파라미터를 딕셔너리로 정의
paramJson = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬 웹크롤링'
}

response2 = requests.get('https://section.blog.naver.com/Search/Post.naver', params=paramJson)
# print(response2.status_code) # 응답코드를 출력
# print(response2.text) # HTML 코드를 출력

# 뷰티풀숩 모드 임포트
from bs4 import BeautifulSoup

# requests 모듈을 이용해서 페이지 정보 얻어오기
url = 'http://daum.net/'
response = requests.get(url)

# 응답코드가 200이면 정상적으로 응답이 온것이므로..
if response.status_code == 200:
  # 뷰티풀숩 객체로 변환한다.
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else : 
    # 통신에 문제가 생겼다면 응답코드를 출력해서 확인해본다.
    print(response.status_code)


'''
#s_content > div.section > ul > li:nth-child(1) > dl > dt > a > b
'''
