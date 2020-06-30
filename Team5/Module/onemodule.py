from crawler import SeleniumRequest
from pprint import pprint
import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

test = input("도시를 선택하세요. :")
whoru = input("성별을 입력하세요. (남성, 여성):")

if test == '서울':
    #서울 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

elif test == '부산':
    #부산 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Busan&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

else:
    print("종료")

style = a

print("현재", test, "의 날씨는", a, "도 입니다.")
print("사용자의 성별은", whoru, "입니다.")

if style > 27:
    if whoru == '남성':
        response = urlopen('https://rodenty.com/product/search.html?banner_action=&keyword=%EB%B0%98%ED%8C%94')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("남성반팔.txt", 'w')
        for anchor in soup.select("div.description > ul.name > li > a > span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
        response = urlopen('https://rodenty.com/product/search.html?banner_action=&keyword=%EB%B0%98%EB%B0%94%EC%A7%80')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("남성반바지.txt", 'w')
        for anchor in soup.select("div.description > ul.name > li > a > span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
    if whoru == '여성':
        response = urlopen('https://codibook.net/search/?search=%EB%B0%98%ED%8C%94&filter=item')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("여성반팔.txt", 'w')
        for anchor in soup.select("a.span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
        response = urlopen('https://codibook.net/search/?search=%EB%B0%98%EB%B0%94%EC%A7%80&filter=item')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("여성반바지.txt", 'w')
        for anchor in soup.select("a.span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()

if style < 28:
    if whoru == '남성':
        response = urlopen('https://rodenty.com/product/search.html?banner_action=&keyword=%EA%B8%B4%ED%8C%94')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("남성긴팔.txt", 'w')
        for anchor in soup.select("div.description > ul.name > li > a > span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
        response = urlopen('https://rodenty.com/product/search.html?banner_action=&keyword=%EB%8D%B0%EB%8B%98')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("남성긴바지.txt", 'w')
        for anchor in soup.select("div.description > ul.name > li > a > span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
    if whoru == '여성':
        response = urlopen('https://codibook.net/search/?search=%EA%B8%B4%ED%8C%94&filter=item')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("여성긴팔팔.txt", 'w')
        for anchor in soup.select("a.span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
        response = urlopen('https://codibook.net/search/?search=%EA%B8%B4%EB%B0%94%EC%A7%80&filter=item')
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        f = open("여성긴바지.txt", 'w')
        for anchor in soup.select("a.span"):
            data = str(i) + ". " + anchor.get_text() + "\n"
            i += 1
            f.write(data)
            if i > 5:
                break
        f.close()
