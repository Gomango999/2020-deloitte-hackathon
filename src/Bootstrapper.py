from src.System import System
from src.Patient import Patient
from src.GP import GP
from src.Symptom import Symptom
from src.Profile import Profile
from src.Response import Response
from src.Question import TextQuestion, TextAreaQuestion, RadioButtonQuestion, CheckBoxQuestion

def bootstrap_system():
    system = System()

    gp = GP(Profile("Jane", "Female", NotImplemented, NotImplemented, NotImplemented))
    patient = Patient(Profile("Robert", "Male", "15/07/1997", "bob@gmail.com", "1"), [])
    system.gp = gp
    system.patient = patient
    questions = [
        TextQuestion("First Name"),
        TextQuestion("Last Name"),
        TextAreaQuestion("What prescription or non-prescription medicine do you take, if any?"),
        TextAreaQuestion("Describe any surgeries you have had in the last 6 months, if any?"),
        TextAreaQuestion("What allergies do you have, if any?"),
        CheckBoxQuestion("Have you used any of these substances recently?", ["Nicotine", "Alcohol", "Illicit Drugs"])
    ]
    questions[0].answer = "Robert"
    questions[1].answer = "Johnson"
    questions[2].answer = "Amoxycillin\nTrimethoprim with sulfamethoxazole\nChlorpromazine"
    questions[3].answer = "25th Jan 2020 - Appendectomy\n13th Feb 2020 - Heart Transplant"
    questions[4].answer = "Shellfish"
    questions[5].answer = [False, True, False]
    system.questions = questions

    symptoms = [
        Symptom("Cough", [
            CheckBoxQuestion("How is your cough?", ["Dry Cough", "Wet Cough", "Chesty Cough"]),
            TextAreaQuestion("How long have you had this symptom?")
        ]),
        Symptom("Headache", [
            CheckBoxQuestion("How is your headache?", ["Numb", "Sharp", "Throbbing"])
        ]),
        Symptom("Fever", [
            RadioButtonQuestion("Have you been overseas in the last 2 weeks?", ["Yes", "No"]),
        ])
    ]
    symptoms[0].questions[0].answer = [False, False, True]
    symptoms[0].questions[1].answer = "2 weeks"
    symptoms[1].questions[0].answer = [False, True, True]
    symptoms[2].questions[0].answer = 0
    system.symptoms = symptoms

    form_token = "PJOCWXHEWOWAMHWKDFYT"
    response = Response(patient, gp, questions, "12/05/20", symptoms, form_token)
    system.set_patient_response(form_token, response)
    return system
