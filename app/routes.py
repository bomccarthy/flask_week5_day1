from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cigars')
def cigar():
    stogie = [{'cigar':'Oscar Habano', 'image':'images/oscar_habano.jpg'},
            {'cigar':'Aladino Vintage Selection', 'image':'images/aladino_vintage_selection.jpg'},
            {'cigar':'My Father Connecticut', 'image':'images/my_father_connecticut.jpg'},
            {'cigar':'EP Carrillo Connecticut', 'image':'images/e_p_carrillo_connecticut.jpg'},
            {'cigar':'Crux Bull & Bear', 'image':'images/crux_bull_and_bear.jpg'}]
    return render_template('cigar.html', cigar=stogie)


@app.route('/sports')
def sports():
    return render_template('sports.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/food')
def food():
    return render_template('food.html')


@app.route('/drinks')
def drink():
    return render_template('drink.html')

