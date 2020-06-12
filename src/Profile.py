class Profile: 
	Questions = {'Family History' : None,
				 'Prescriptions/Drug Use' : None,
				 'Alcohol' : None,
				 'Smoking' : None,
				 }

	def __init__(self, name, gender, date, email, num):
		self.name = name 
		self.gender = gender
		self.date = date
		self.num = num

