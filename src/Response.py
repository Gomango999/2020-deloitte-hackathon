class Response:
    def __init__(self, patient, gp, questions, date, worstsymp, symp):
        self._patient = patient
        self._gp = gp
        self._questions = questions
        self._date = date
        self._worstsymp = worstsymp
        self._symp = symp #symp() constructor

    @property
    def patient(self):
        return self._patient

    @property
    def gp(self):
        return self._gp
    
    @property
    def questions(self):
        return self._questions