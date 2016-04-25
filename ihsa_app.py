from school_list import schools_list
from regions import regions, south, northeast, west, midwest
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import validators, ValidationError
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask.ext.bootstrap import Bootstrap
# ...
app = Flask(__name__)
app.secret_key = 'development key'
bootstrap = Bootstrap(app)

source = schools_list

def state_info(source, state_name):
    state_list = []
    for row in source:
        if state_name == row["State"]:
            team = row["School"]
            coach = row["Coach"]
            detail_list = [team, coach]
            state_list.append(detail_list)
    return state_list

def region1(source):
    regional = []
    for key in source:
        regional.append(key)
    return sorted(regional)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home/search')
def search():
    region_menu = region1(regions)
    return render_template('pickstate.html', region_menu=region_menu)

@app.route('/home/search/<region>')
def show(region):
    for key in regions:
        if key == region:
            states = regions[key]
    return render_template('details.html', states=states, region=region)

@app.route('/home/search/<region>/<state_name>')
def details(region, state_name):
    for key in regions:
        if key == region:
            states = regions[key]
    state_list = state_info(source, state_name)
    return render_template('details.html', state_list=state_list, state_name=state_name, region=region, states=states)



#if __name__ == '__main__':
#    app.run(debug=True)
