class Patient:
    def __init__(self, profile, responses):
        self._profile = profile
        self._responses = []

    def addResponse(self, response):
        self._response[self._responses.len()] = response

    @property
    def name(self):
        return self._profile._name
