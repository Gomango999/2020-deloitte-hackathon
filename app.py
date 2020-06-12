from flask import Flask, render_template, request
import requests
import json
import re
import copy

from src.Bootstrapper import bootstrap_system
from src.Response import Response

app = Flask(__name__)
app.debug = True

system = bootstrap_system()

@app.route('/')
def index():
    return render_template('index.html', a=system.a)

@app.route('/patient_form/<form_token>')
def patient_form(form_token):
    # response = system.get_patient_response(form_token)
    return render_template('patient.html', patient=system.patient, system=system, form_token=form_token)


# ImmutableMultiDict([('General-0', ''), ('General-1', ''), ('General-3', ''), ('General-3', ''), ('Symptom-Cough', 'Cough'), ('Cough-0-0', '1'), ('Cough-0-1', '1'), ('Cough-1', ''), ('Headache-1', ''), ('Fever-0', ''), ('Fever-1', '')])
# general- is for general questions
# symptom- is for selected symptoms
# X- is for all other symptoms. We extract the number afterwards for the question number

@app.route('/submitted', methods=["POST"])
def submitted():
    if request.method == 'POST':
        print(request.form)
        # Make a response object and populate it with information from the request.form
        questions = system.questions.copy()
        symptoms = []
        form_token = ""
        for key in request.form:
            value = request.form[key]
            print(key, value)

            if 'form_token' in key:
                form_token = value
            elif 'General' in key:
                numbers = list(map(int, re.findall('\d+',key)))
                print(numbers)
                question_number = numbers[0]
                question = questions[question_number]
                if len(numbers) == 1:
                    question.set_answer(value)
                elif len(numbers) == 2:
                    question_part = numbers[1]
                    if int(value) == 1:
                        question.set_answer(question_part)
            elif 'Symptom' in key:
                name = key.split('-')[1]
                symptom = system.get_symptom(name)
                symptoms.append(copy.deepcopy(symptom))
            else:
                name = key.split('-')[0]
                numbers = list(map(int, re.findall('\d+',key)))
                for symptom in symptoms:
                    if symptom.name.lower() == name.lower():
                        question_number = numbers[0]
                        question = symptom.questions[question_number]
                        if len(numbers) == 1:
                            question.set_answer(value)
                        elif len(numbers) == 2:
                            question_part = numbers[1]
                            if int(value) == 1:
                                question.set_answer(question_part)

        response = Response(system.patient, system.gp, system.questions, "13/06/20", symptoms, form_token)
        system.set_patient_response(form_token, response)
        return render_template('submitted.html', response=response)

@app.route('/gp/<name>')
def gp_page(name):
    responses = list(filter(lambda i: i[1].gp.name == name, system._patient_responses.items()))
    return render_template('gp.html', responses=responses)


@app.route('/form_gp_view/<form_token>')
def form_gp_view(form_token):
    response = system._patient_responses[form_token]
    return render_template('form_gp_view.html', response=response)
