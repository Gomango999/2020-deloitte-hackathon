class Patient:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
'''
Since it's not good convention yet
class Patient:
	def __init__(self, profile, responses):
		self.profile = profile
		self.numresps = 0
		self.responses = []

	def addResponse(self, response):
		self.response[self.numresps] = response
		self.numresps += 1
'''
