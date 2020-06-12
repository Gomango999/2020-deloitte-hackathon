from flask import Flask, render_template, request
import requests
import json
from src.Bootstrapper import bootstrap_system

app = Flask(__name__)
app.debug = True

system = bootstrap_system()

@app.route('/')
def index():
    return render_template('index.html', a=system.a)

@app.route('/patient_form/<form_token>')
def patient_form(form_token):
    response = system.get_patient_response(form_token)
    return render_template('patient.html', response=response)