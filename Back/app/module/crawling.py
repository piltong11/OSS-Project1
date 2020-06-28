import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

def style(temp, gender):
    if temp > 25:
        if gender == '남성':
            urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EB%B0%98%ED%8C%94"
            req = urllib.request.Request(urlsite)
            sourcecode = urllib.request.urlopen(urlsite).read()
            soup = BeautifulSoup(sourcecode, "html.parser")
            i = 1
            f = open("./app/module/link/man-tshirt-href.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https://rodenty.com" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/man-tshirt-img.txt", 'w')
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
            f = open("./app/module/link/man-pants-href.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https://rodenty.com" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/man-pants-img.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https:" + href.find("img")["src"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

        elif gender == '여성':
            urlsite = "https://ko.codibook.net/search/?search=%EB%B0%98%ED%8C%94&filter="
            req = urllib.request.Request(urlsite)
            sourcecode = urllib.request.urlopen(urlsite).read()
            soup = BeautifulSoup(sourcecode, "html.parser")
            i = 1
            f = open("./app/module/link/woman-tshirt-href.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/woman-tshirt-img.txt", 'w')
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
            f = open("./app/module/link/woman-pants-href.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/woman-pants-img.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = href.find("img")["src"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

    elif temp <= 25:
        if gender == '남성':
            urlsite = "https://rodenty.com/product/search.html?banner_action=&keyword=%EA%B8%B4%ED%8C%94"
            req = urllib.request.Request(urlsite)
            sourcecode = urllib.request.urlopen(urlsite).read()
            soup = BeautifulSoup(sourcecode, "html.parser")
            i = 1
            f = open("./app/module/link/man-longshirt-href.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https://rodenty.com" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/man-longshirt-img.txt", 'w')
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
            f = open("./app/module/link/man-longpants-href.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https://rodenty.com" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/man-longpants-img.txt", 'w')
            for href in soup.find("ul", class_="prdList grid3").find_all("div", class_="thumbnail"):
                data = "https:" + href.find("img")["src"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

        elif gender == '여성':
            urlsite = "https://ko.codibook.net/search/?search=%EA%B8%B4%ED%8C%94&filter="
            req = urllib.request.Request(urlsite)
            sourcecode = urllib.request.urlopen(urlsite).read()
            soup = BeautifulSoup(sourcecode, "html.parser")
            i = 1
            f = open("./app/module/link/woman-longshirt-href.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/woman-longshirt-img.txt", 'w')
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
            f = open("./app/module/link/woman-longpants-href.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = "https://ko.codibook.net" + href.find("a")["href"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()

            i = 1
            f = open("./app/module/link/woman-longpants-img.txt", 'w')
            for href in soup.find("div", class_="item_list").find_all("div", class_="set item"):
                data = href.find("img")["src"] + "\n"
                i += 1
                f.write(data)
                if i > 6:
                    break
            f.close()
