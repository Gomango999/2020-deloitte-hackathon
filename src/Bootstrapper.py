from src.System import System
from src.Patient import Patient
from src.GP import GP
from src.Symptom import Symptom
from src.Profile import Profile
from src.Response import Response
from src.Question import TextQuestion, RadioButtonQuestion, CheckBoxQuestion

def bootstrap_system():
    system = System()
    system.a = 5

    g = GP(Profile("Jane", "Female", NotImplemented, NotImplemented, NotImplemented))
    p = Patient(Profile("Robert", "Male", "15/07/1997", "bob@gmail.com", "1"), [])
    questions = [
        TextQuestion("First Name"),
        TextQuestion("Last Name"),
        TextQuestion("What prescription or non-prescription medicine do you take, if any?"),
        TextQuestion("Describe any surgeries you have had in the last 6 months, if any?"),
        TextQuestion("What allergies do you have, if any?"),
        CheckBoxQuestion("Have you used any of these substances recently?", ["Nicotine", "Alcohol", "Illicit Drugs"])
    ]
    questions[0].answer = "Robert"
    questions[1].answer = "Johnson"
    questions[2].answer = "Amoxycillin\nTrimethoprim with sulfamethoxazole\nChlorpromazine"
    questions[3].answer = "25th Jan Appendectomy\n13th Feb 2020 Heart Transplant"
    questions[4].answer = "Shellfish"
    questions[5].answer = [False, True, False]

    symptoms = [
        Symptom("Cough",
        [RadioButtonQuestion("How is your cough?", ["Dry", "Wet"]),
         TextQuestion("How long have you had this symptom?")
        ]),
        Symptom("Headache",
        [RadioButtonQuestion("How is your headache?", ["Numb", "Sharp"]),
         TextQuestion("How long have you had this symptom?")
        ]),
        Symptom("Fever",
        [TextQuestion("What was your peak temperature?"),
         TextQuestion("How long have you had this symptom?")
        ])
    ]
    

    r = Response(p, g, questions, NotImplemented, symptoms)
    system.set_patient_response("aaa", r)
    return system
