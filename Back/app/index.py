from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

cover = Blueprint('cover', __name__, url_prefix='/')
option = Blueprint('option', __name__, url_prefix='/')
weather = Blueprint('weather', __name__, url_prefix='/')
fashion = Blueprint('fashion', __name__, url_prefix='/')

@cover.route('/cover',methods=['GET'])
def index():

    #DB 관련 쿼리문 작성
    #변수에 값을 담아서 html과 같이 랜더링

    return render_template('/cover.html')

@option.route('/option',methods=['GET'])
def index():

    #DB 관련 쿼리문 작성
    #변수에 값을 담아서 html과 같이 랜더링

    return render_template('/option.html')

@weather.route('/weather',methods=['GET'])
def index():

    #DB 관련 쿼리문 작성
    #변수에 값을 담아서 html과 같이 랜더링

    return render_template('/weather.html')

@fashion.route('/fashion',methods=['GET'])
def index():

    picture1 = '사진1.jpg'
    picture2 = '사진2.jpg'

    return render_template('/fashion.html', p1 = picture1, p2 = picture2)
