from abc import ABC,abstractmethod

class AbstractController(ABC):
    @abstractmethod
    def set_operation(self, operation):
        pass

    @abstractmethod
    def calculate(self, num1, num2):
        pass

    @abstractmethod
    def get_result(self):
        pass

