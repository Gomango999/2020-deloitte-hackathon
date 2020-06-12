class System:
    def __init__(self):
        self._a = 0

    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, a):
        self._a = a
