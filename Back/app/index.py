from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module import dbModule
from app.module import temp

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

    gender = request.form['gender']
    place = request.form['place']
    temperature = temp.getTemp(place)

    return render_template('/weather.html', g=gender, p=place, t=temperature)

@fashion.route('/fashion',methods=['GET'])
def index():

    db = dbModule.DB()

    #sql = 쿼리문 작성
    #result = db.executeAll(sql)

    picture1 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'
    picture2 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'
    picture3 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'
    picture4 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'
    picture5 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'
    picture6 = 'https://rodenty.com/web/product/medium/20200627/10e3a0f3aa2d20401f391714f9c16968.jpg'

    return render_template('/fashion.html', p1 = picture1, p2 = picture2, p3 = picture3,
                                            p4 = picture4, p5 = picture5, p6 = picture6)
