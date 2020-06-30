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
    
elif test == '인천':
    #인천 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Incheon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

elif test == '대전':
    #대전 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Daejeon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"

    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]


elif test == '울산':
    #울산 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Ulsan&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
    
    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

elif test == '대구':
    #대구 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Daegu&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
    
    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

elif test == '광주':
    #광주 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Gwangju&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
    
    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]

elif test == '춘천':
    #춘천 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Chuncheon&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
    
    url=api.format()
    #api에 요청을 보내 데이터 추출
    res = requests.get(url)
    #결과값을 Json형식으로 변환
    data = json.loads(res.text)
    #날씨 정보
    print("")
    a = data["list"][3]["main"]["temp"]


elif test == '제주도':
    #제주도 키값
    api = api = "https://api.openweathermap.org/data/2.5/forecast?q=Jeju&appid=2ae7d290dffcdea9ae07b40a37d57d65&units=metric&lang=kr"
    
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
