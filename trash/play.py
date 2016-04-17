from school_list import schools_list
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import validators, ValidationError
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'development key'
bootstrap = Bootstrap(app)

#def lists(source):
#    locations = []
#    for row in source:
#        state = row["State"]
#        locations.append(state)
#    return sorted(locations)

#info = lists(schools_list)
#print(info)

def schools(source):
    #schools = []
    #for row in source:
    #    school = row["School"]
    #    schools.append(school)
    #return sorted(schools)
    region = ['NE', 'SE', 'SW', 'NW']
    southeast = ['FL', 'AL', 'GA']
    #if region == 'SE':
    for row in source:
        state = row["State"]
        if "FL" == southeast:
            team = row["School"]
            coach = row["Coach"]
            return state, team, coach
#info2 = schools(schools_list)
#print(info2

#region = ['NE', 'SE', 'SW', 'NW']
#southeast = ['FL', 'AL', 'GA']

#def getting_it(source):
#    region = ['NE', 'SE', 'SW', 'NW']
#    southeast = ['FL', 'AL', 'GA']
#    if region == 'SE':
#        for row in source:
#            state = row["State"]
#            if state == southeast:
#                team = row["School"]
#                coach = row["Coach"]
#            return state, team, coach

please = schools(schools_list)
print(please)

#    for row in source:
#        if <li> == row["State"]:
#            team = row["School"]
#            coach = row["Coach"]
