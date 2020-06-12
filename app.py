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

@app.route('/gp/<name>')
def gp_page(name):
    responses = list(filter(lambda i: i[1].gp.name == name, system._patient_responses.items()))
    return render_template('gp.html', responses=responses)


@app.route('/form_gp_view/<form_token>')
def form_gp_view(form_token):
    response = system._patient_responses[form_token]
    return render_template('form_gp_view.html', response=response)