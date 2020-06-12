from src.System import System
from src.Patient import Patient
from src.GP import GP
from src.Response import Response

def bootstrap_system():
    system = System()
    system.a = 5

    g = GP()
    p = Patient("Bob")
    r = Response(p, g, NotImplemented, NotImplemented, NotImplemented)
    system.set_patient_response("aaa", r)
    return system
