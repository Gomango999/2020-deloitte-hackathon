class Response:
    def __init__(self, patient, gp, questions, date, symptoms):
        self._patient = patient
        self._gp = gp
        self._date = date
        self._symptoms = symptoms
        self._questions = questions # Should be constant

    def addsymptoms(symptoms):
        self._symptoms.append(symptoms)

    @property
    def symptoms(self):
        return self._symptoms

    @property
    def patient(self):
        return self._patient

    @property
    def gp(self):
        return self._gp

    @property
    def questions(self):
        return self._questions
