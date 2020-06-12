class Patient:
    def __init__(self, profile, responses):
        self.profile = profile
	self.numresps = 0
	self.responses = []
	
    def addResponse(self, response):
	self.response[self.numresps] = response
	self.numresps += 1
    
    @property
    def name(self):
        return self.profile.name
