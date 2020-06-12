class Patient:
    def __init__(self, profile, responses):
        self._profile = profile
	self._numresps = 0
	self._responses = []
	
    def addResponse(self, response):
	self._response[self.numresps] = response
	self._numresps += 1
    
    @property
    def name(self):
        return self._profile._name
