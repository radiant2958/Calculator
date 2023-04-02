
from abc import ABC,abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass