from abc import ABC, abstractmethod

class AbstractModel:
    @abstractmethod
    def __init__(self):
        self.result=0

    @abstractmethod
    def set_operation(self):
        pass
    @abstractmethod
    def calculate(self, num1, num2):
        pass

    @abstractmethod
    def set_numbers(self,num1, num2):
        pass

    @abstractmethod
    def get_result(self):
        pass
   
