from abc import ABC

def Question(ABC):
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer
    
    @property
    def question(self):
        return self._question
    
    @property
    def answer(self):
        return self._answer
    
    @answer.setter
    def answer(self, answer):
        self._answer = answer

def TextQuestion(Question):
    def __init__(self, question):
        super(question, "")

def CheckBoxQuestion(Question):
    def __init__(self, question, choices):
        """
        Choices: List[str]
        """
        self._choices = choices
        super(question, [])
    
    @property
    def choices(self):
        return self._choices

def RadioButtonQuestion(Question):
    def __init__(self, question, choices):
        self._choices = choices
        super(question, "")
    
    @property
    def choices(self):
        return self._choices