class GP:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
   '''
   Bad convention
   class GP:
	"""docstring for ClassName"""
	def __init__(self, name, email, num):
		self.name = name
		self.email = email
		self.num = num
		self.profile = Profile(name, gender, date, email, num)
		self.patients = []
		self.numpts = 0

	def addPt(self, patient):
		self.patients[self.numpts] = patient
		self.numpts += 1
'''
