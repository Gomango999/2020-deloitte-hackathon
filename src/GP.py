class GP:
    def __init__(self, name):
        self._name = name
	self._email = email	
	self._num = num
	self._profile = Profile(name, gender, date, email, num)
	self._patients = []
    	
    def addPt(self, patient):
	self._patients[self._patients.len()] = patient
	
    @property
    def name(self):
        return self._name
