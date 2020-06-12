class System:
    def __init__(self):
        self._a = 0
        self._patient_responses = {}

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a
    
    def get_patient_response(self, token):
        return self._patient_responses[token]
    
    def set_patient_response(self, token, response):
        self._patient_responses[token] = response
