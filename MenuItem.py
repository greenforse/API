from abc import ABCMeta, abstractmethod
class MenuItem(metaclass=ABCMeta):
    def __init__(self,number,title):
        self.number=number
        self.title=title
    def get_number(self,number):
        return self.number
    def get_title(self):
        return self.title
    @abstractmethod
    def execute(self):
        pass
    #def printL(self):
    #    print(f"{self.number}. {self.title}")
    