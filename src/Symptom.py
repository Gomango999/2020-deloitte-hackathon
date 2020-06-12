class Symptom:
	def __init__(self, name, questions):
		self._name = name
		self._questions = questions
	
	@property
	def name(self):
		return self._name

	@property
	def questions(self):
		return self._questions
