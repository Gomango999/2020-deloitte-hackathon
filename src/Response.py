class Response:
	def __init__(self, patient, gp, questions, date, symp):
		self._patient = patient
		self._gp = gp
		self._date = date
		self._symp = symp
		self._questions = questions # Should be constant

	def addSymp(symptom):
		self._symp[self._symp.len()] = symptom

	@property
	def patient(self):
		return self._patient

	@property
	def gp(self):
		return self._gp

	@property
	def questions(self):
		return self._questions
