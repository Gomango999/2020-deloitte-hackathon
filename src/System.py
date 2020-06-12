class System:
    def __init__(self):
        self._a = 0
        self._patient_responses = {}
        #self._gps = []
        #self._pts = []
        #self._symps = []


    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a
    
    def get_patient_response(self, token):
        return self._patient_responses[token]
    
    def set_patient_response(self, token, response):
        self._patient_responses[token] = response

    '''
    def addpatient(self, patient):
        self._pts[self._pts.len()] = patient

    def addgp(self, gp):
        self._gps[self._gps.len()] = gp

    def addsymp(self, symp):
        self._symps[self._symps.len()] = symp
    '''
