import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/lt645/result'
response = requests.get(url)

if response.status_code==200:
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  title1_1 = soup.select_one('#swiperDiv > div.swiper-slide.swiper-slide-active > div > div.result-ballWrapper > div.result-ballBox')
  print("추출1:", title1_1)


else:
  print("응답없음")
  


