import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://music.bugs.co.kr/chart' 
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
# songs = soup.select('table.byChart > tbody > tr')
songs = soup.select('#CHARTrealtime > table > tbody > tr')
for song in songs:
  title = song.select('p.title > a')[0].text # > a(앞에 것 전체를 표시함을 의미)
  singer = song.select('p.artist > a')[0].text
  album = song.select('td:nth-child(9) > a')[0].text
  print(title, singer, sep="|")
  song_data.append([rank, title, singer, album])
  rank = rank + 1
  
columns = ['순위', '곡', '아티스트', '앨범']  
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)
  
  
  
'''
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url = 'https://music.bugs.co.kr/chart'
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


song_data = []
rank = 1


#songs = soup.select('table.byChart > tbody > tr')
songs = soup.select('#CHARTrealtime > table > tbody > tr')
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    album = song.select('td:nth-child(9) > a')[0].text
       
    print(title, singer, album, sep="|")
    song_data.append (['Bugs', rank, title, singer, album])
    rank = rank + 1
   
columns = ['서비스', '순위', '타이틀', '가수', '앨범']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)
'''
  