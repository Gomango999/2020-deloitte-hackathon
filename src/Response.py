class Response:
    def __init__(self, patient, gp):
        self._patient = patient
        self._gp = gp
    
    @property
    def patient(self):
        return self._patient
