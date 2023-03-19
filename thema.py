import requests
from bs4 import BeautifulSoup

for index in range(7):    
    url = "https://finance.naver.com/sise/theme.naver?field=name&ordering=desc&page="+str(index)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # 특정 클래스의 내용을 추출하는 코드
    contents = soup.find_all("td", class_="col_type1")
    for content in contents:
        print(content.find("a").text)   