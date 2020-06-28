import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

test = input("도시를 선택하세요. :")
whoru = input("성별을 입력하세요. (남성, 여성):")

if test == '서울':
    #서울 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url = api.format()
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

    url = api.format()
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
        urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EB%B0%98%ED%8C%94"
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("남성반팔.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https://rodenty.com" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("남성반팔사진.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https:" + href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EB%B0%98%EB%B0%94%EC%A7%80"
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("남성반바지.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https://rodenty.com" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("남성반바지사진.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https:" + href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

    if whoru == '여성':
        urlsite = "https://ko.codibook.net/search/?search=%EB%B0%98%ED%8C%94&filter="
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("여성반팔.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("여성반팔사진.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        urlsite = "https://ko.codibook.net/search/?search=%EB%B0%98%EB%B0%94%EC%A7%80&filter="
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("여성반바지.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("여성반바지사진.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

if style < 28:
    if whoru == '남성':
        urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EA%B8%B4%ED%8C%94"
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("남성긴팔.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https://rodenty.com" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("남성긴팔사진.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https:" + href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EB%8D%B0%EB%8B%98"
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("남성긴바지.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https://rodenty.com" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("남성긴바지사진.txt", 'w')
        for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
            data = "https:" + href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

    if whoru == '여성':
        urlsite = "https://ko.codibook.net/search/?search=%EA%B8%B4%ED%8C%94&filter="
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("여성긴팔.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("여성긴팔사진.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        urlsite = "https://ko.codibook.net/search/?search=%EA%B8%B4%EB%B0%94%EC%A7%80&filter="
        req = urllib.request.Request(urlsite)
        sourcecode = urllib.request.urlopen(urlsite).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        i = 1
        f = open("여성긴바지.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()

        i = 1
        f = open("여성긴바지사진.txt", 'w')
        for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
            data = href.find("img")["src"] + "\n"
            i += 1
            f.write(data)
            if i > 6:
                break
        f.close()
