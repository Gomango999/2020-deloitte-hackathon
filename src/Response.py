class Response:
    def __init__(self, patient, gp, date, worstsymp):
        self._patient = patient
        self._gp = gp
        self._questions = questions
        self._date = date
        self._worstsymp = worstsymp
        self._symp = []
	self._questions = []
        
    def addSymp(symptom):
	self._symp[self._symp.len()] = symptom

    def addQues(question):
	self._questions[self._questions.len()] = question
        
    @property
    def patient(self):
        return self._patient

    @property
    def gp(self):
        return self._gp
    
    @property
    def questions(self):
        return self._questions
 
