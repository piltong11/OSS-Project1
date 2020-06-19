import requests
import json

test =input( "도시를 선택하세요. :" )

if test == 'Seoul':
    #서울 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("도시=", data["city"]["name"])
    print("예측시간=", data["list"][3]["dt_txt"])
    print("기온=", data["list"][3]["main"]["temp"])
    print("날씨=", data["list"][3]["weather"])
    print("습도=", data["list"][3]["main"]["humidity"],"%")
    print("바람=", data["list"][3]["wind"]["speed"],"m/s")
    print("")

elif test == 'Busan':
    #부산 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Busan&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("도시=", data["city"]["name"])
    print("예측시간=", data["list"][3]["dt_txt"])
    print("기온=", data["list"][3]["main"]["temp"])
    print("날씨=", data["list"][3]["weather"])
    print("습도=", data["list"][3]["main"]["humidity"],"%")
    print("바람=", data["list"][3]["wind"]["speed"],"m/s")
    print("")

else:
    print("종료")
