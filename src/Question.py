from abc import ABC, abstractmethod

class Question(ABC):
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
    
    @abstractmethod
    def questionType(self):
        """ Convenience method for Jinja """
        raise NotImplementedError

class TextQuestion(Question):
    def __init__(self, question):
        super().__init__(question, "")
    
    def questionType(self):
        return "text"

class CheckBoxQuestion(Question):
    def __init__(self, question, choices):
        """
        Choices: List[str]
        """
        self._choices = choices
        super().__init__(question, [])
    
    @property
    def choices(self):
        return self._choices

    def questionType(self):
        return "check"

class RadioButtonQuestion(Question):
    def __init__(self, question, choices):
        self._choices = choices
        super().__init__(question, 0)
    
    @property
    def choices(self):
        return self._choices
    
    def questionType(self):
        return "radio"