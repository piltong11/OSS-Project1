import requests
import json

#api주소값
api = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

#도시
cities = ["Seoul", "Busan"]


    #api주소
for name in cities:
    url=api.format(city=name)
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)


    print("도시=", data["city"]["name"])
    print("예측시간=", data["list"][3]["dt_txt"])
    print("기온=", data["list"][3]["main"]["temp"])
    print("날씨=", data["list"][3]["weather"])
    print("습도=", data["list"][3]["main"]["humidity"],"%")
    print("바람=", data["list"][3]["wind"]["speed"],"m/s")
    print("")

    print("예측시간=", data["list"][11]["dt_txt"])
    print("기온=", data["list"][11]["main"]["temp"])
    print("날씨=", data["list"][11]["weather"])
    print("습도=", data["list"][11]["main"]["humidity"],"%")
    print("바람=", data["list"][11]["wind"]["speed"],"m/s")
    print("")

    print("예측시간=", data["list"][19]["dt_txt"])
    print("기온=", data["list"][19]["main"]["temp"])
    print("날씨=", data["list"][19]["weather"])
    print("습도=", data["list"][19]["main"]["humidity"],"%")
    print("바람=", data["list"][19]["wind"]["speed"],"m/s")
    print("")

    print("예측시간=", data["list"][27]["dt_txt"])
    print("기온=", data["list"][27]["main"]["temp"])
    print("날씨=", data["list"][27]["weather"])
    print("습도=", data["list"][27]["main"]["humidity"],"%")
    print("바람=", data["list"][27]["wind"]["speed"],"m/s")
    print("")

    print("예측시간=", data["list"][35]["dt_txt"])
    print("기온=", data["list"][35]["main"]["temp"])
    print("날씨=", data["list"][35]["weather"])
    print("습도=", data["list"][35]["main"]["humidity"],"%")
    print("바람=", data["list"][35]["wind"]["speed"],"m/s")
    print("")
    print("----------------------------------------------")
