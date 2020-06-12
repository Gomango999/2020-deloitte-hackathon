class Profile: 
	Questions = {'Family History' : None,
				 'Prescriptions/Drug Use' : None,
				 'Alcohol' : None,
				 'Smoking' : None,
				 }

	def __init__(self, name, gender, date, email, num):
		self._name = name 
		self._gender = gender
		self._date = date
		self._num = num

