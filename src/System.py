class System:
    def __init__(self):
        self._a = 0
        self._patient_responses = {}
        self._symptoms = []
        self._questions = []


    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, a):
        self._a = a

    @property
    def symptoms(self):
        return self._symptoms
    @symptoms.setter
    def symptoms(self, symptoms):
        self._symptoms = symptoms

    @property
    def questions(self):
        return self._questions
    @questions.setter
    def questions(self, questions):
        self._questions = questions

    def get_patient_response(self, token):
        return self._patient_responses[token]

    def set_patient_response(self, token, response):
        self._patient_responses[token] = response

    def get_symptom(self, name):
        for symptom in self._symptoms:
            if symptom.name.lower() == name.lower():
                return symptom
        return None

    '''
    def addpatient(self, patient):
        self._pts[self._pts.len()] = patient

    def addgp(self, gp):
        self._gps[self._gps.len()] = gp

    def addsymp(self, symp):
        self._symps[self._symps.len()] = symp
    '''
