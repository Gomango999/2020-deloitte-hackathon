class GP:
	def __init__(self, profile):
		self._profile = profile
		self._patients = []

	def addPt(self, patient):
		self._patients[self._patients.len()] = patient

	@property
	def name(self):
		return self._profile._name
