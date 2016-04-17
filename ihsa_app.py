from school_list import schools_list
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import validators, ValidationError
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask.ext.bootstrap import Bootstrap
# ...
app = Flask(__name__)
app.secret_key = 'development key'
bootstrap = Bootstrap(app)


def list_schools(source):
    locations = []
    for row in source:
        location = row["State"]
        locations.append(location)
    return sorted(locations)

#location_only = list_schools(schools_list)
#print(location_only)

def state_info(source, state):
    for row in source:
        if state == row["State"]:
            team = row["School"]
            coach = row["Coach"]
            return state, team, coach


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home/search')
def search():
    location_only = list_schools(schools_list)
    return render_template('pickstate.html', location_only=location_only)

@app.route('/home/search/<state>')
def find(state):
    state, team, coach = state_info(schools_list, state)
    return render_template('details.html', state=state, team=team, coach=coach)


if __name__ == '__main__':
    app.run(debug=True)
