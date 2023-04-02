
from Controller.AbstractController import AbstractController
from Operation.DivideOperation import DivideOperation
from Model.Model import Model
from Operation.MultiplyOperation import MultiplyOperation
from Operation.SubtractOperation import SubtractOperation
from Operation.SumOperation import SumOPeration


class Controller(AbstractController):
    def __init__(self):
        self.model = Model()
       


    
    def calculate(self, num1, num2):
        self.model.calculate(num1, num2)
    
    def set_operation(self, operation):
        if operation == "+":
            self.operation = SumOPeration()
        elif operation == "-":
            self.operation = SubtractOperation()
        elif operation == "*":
            self.operation = MultiplyOperation()
        elif operation == "/":
            self.operation = DivideOperation()
        else:
            raise ValueError("такой операции нет")
        self.model.set_operation(self.operation)
        
    def get_result(self):
        return self.model.get_result()

       





