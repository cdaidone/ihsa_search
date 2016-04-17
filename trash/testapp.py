import schools
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import validators, ValidationError
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask.ext.bootstrap import Bootstrap

print(schools)
