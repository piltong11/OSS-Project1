from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module import temp
from app.module import crawling

cover = Blueprint('cover', __name__, url_prefix='/')
option = Blueprint('option', __name__, url_prefix='/')
weather = Blueprint('weather', __name__, url_prefix='/')
fashion = Blueprint('fashion', __name__, url_prefix='/')

@cover.route('/cover',methods=['GET'])
def index():

    return render_template('/cover.html')

@option.route('/option',methods=['GET'])
def index():

    return render_template('/option.html')

@weather.route('/weather',methods=['POST'])
def index():

    global gender
    global place
    gender = request.form['gender']
    place = request.form['place']
    #기상정보 획득
    temperature = temp.getTemp(place)

    return render_template('/weather.html', g=gender, p=place, t=temperature)

@fashion.route('/fashion',methods=['GET'])
def index():

    #기상정보 획득
    temperature = temp.getTemp(place)
    #패션정보 크롤링
    crawling.style(temperature,gender)
    #파일정보 읽기
    if temperature > 25 :
        if gender=='남성':
            f = open("./app/module/link/man-tshirt-href.txt", "r")
            href1 = f.readline()
            href2 = f.readline()
            href3 = f.readline()
            f.close()

            f = open("./app/module/link/man-pants-href.txt", "r")
            href4 = f.readline()
            href5 = f.readline()
            href6 = f.readline()
            f.close()

            f = open("./app/module/link/man-tshirt-img.txt", "r")
            img1 = f.readline()
            img2 = f.readline()
            img3 = f.readline()
            f.close()

            f = open("./app/module/link/man-pants-img.txt", "r")
            img4 = f.readline()
            img5 = f.readline()
            img6 = f.readline()
            f.close()

        elif gender=='여성':
            f = open("./app/module/link/woman-tshirt-href.txt", "r")
            href1 = f.readline()
            href2 = f.readline()
            href3 = f.readline()
            f.close()

            f = open("./app/module/link/woman-pants-href.txt", "r")
            href4 = f.readline()
            href5 = f.readline()
            href6 = f.readline()
            f.close()

            f = open("./app/module/link/woman-tshirt-img.txt", "r")
            img1 = f.readline()
            img2 = f.readline()
            img3 = f.readline()
            f.close()


            f = open("./app/module/link/woman-pants-img.txt", "r")
            img4 = f.readline()
            img5 = f.readline()
            img6 = f.readline()
            f.close()

    elif temperature <= 25 :
        if gender=='남성':
            f = open("./app/module/link/man-longshirt-href.txt", "r")
            href1 = f.readline()
            href2 = f.readline()
            href3 = f.readline()
            f.close()

            f = open("./app/module/link/man-longpants-href.txt", "r")
            href4 = f.readline()
            href5 = f.readline()
            href6 = f.readline()
            f.close()

            f = open("./app/module/link/man-longshirt-img.txt", "r")
            img1 = f.readline()
            img2 = f.readline()
            img3 = f.readline()
            f.close()

            f = open("./app/module/link/man-longpants-img.txt", "r")
            img4 = f.readline()
            img5 = f.readline()
            img6 = f.readline()
            f.close()

        elif gender=='여성':
            f = open("./app/module/link/woman-longshirt-href.txt", "r")
            href1 = f.readline()
            href2 = f.readline()
            href3 = f.readline()
            f.close()

            f = open("./app/module/link/woman-longpants-href.txt", "r")
            href4 = f.readline()
            href5 = f.readline()
            href6 = f.readline()
            f.close()

            f = open("./app/module/link/woman-longshirt-img.txt", "r")
            img1 = f.readline()
            img2 = f.readline()
            img3 = f.readline()
            f.close()


            f = open("./app/module/link/woman-longpants-img.txt", "r")
            img4 = f.readline()
            img5 = f.readline()
            img6 = f.readline()
            f.close()

    return render_template('/fashion.html', i1=img1, i2=img2,
                                            i3=img3, i4=img4,
                                            i5=img5, i6=img6,
                                            h1=href1, h2=href2,
                                            h3=href3, h4=href4,
                                            h5=href5, h6=href6)
