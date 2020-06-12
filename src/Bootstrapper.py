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
    questions = [] 
    r = Response(p, g, NotImplemented, NotImplemented, NotImplemented)
    system.set_patient_response("aaa", r)
    return system
