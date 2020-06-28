import requests
import json

def getTemp(input):
    if input == '서울':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '부산':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Busan&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '대구':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Daegu&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '인천':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Incheon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '광주':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Gwangju&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '대전':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Daejeon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '울산':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Ulsan&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)

    elif input == '춘천':
        #서울 키값
        api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Chuncheon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
        url=api.format()
        #api에 요청을 보내 데이터 추출
        res = requests.get(url)
        #결과값을 Json형식으로 변환
        data = json.loads(res.text)
        value = data["list"][3]["main"]["temp"]

        return round(value,1)
