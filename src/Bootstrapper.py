from src.System import System
from src.Patient import Patient
from src.GP import GP
from src.Response import Response
from src.Question import TextQuestion, RadioButtonQuestion, CheckBoxQuestion

def bootstrap_system():
    system = System()
    system.a = 5

    g = GP("Jane")
    p = Patient("Bob")
    questions = [TextQuestion("Are you alive?"), RadioButtonQuestion("can u read this?", ["No", "Yes"]), CheckBoxQuestion("Question 3", ["0", "1"])]
    questions[0].answer = "No"
    questions[1].answer = 0
    questions[2].answer = [True, True]

    r = Response(p, g, questions, NotImplemented, NotImplemented, NotImplemented)
    system.set_patient_response("aaa", r)
    return system
