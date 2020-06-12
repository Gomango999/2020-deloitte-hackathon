class GP:
    def __init__(self, name, email, num):
	self._profile = Profile(name, none, none, email, num)
	self._patients = []
    	
    def addPt(self, patient):
	self._patients[self._patients.len()] = patient
	
    @property
    def name(self):
        return self._name
