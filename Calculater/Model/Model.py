from Model.AbstractModel import AbstractModel


class Model(AbstractModel):
    def __init__(self):
        self.result= 0
        self.operation = None
        self.num1=None
        self.num2=None

    def set_operation(self, operation):
        self.operation=operation

    def calculate(self, num1, num2):
        self.result =  self.operation.execute(num1, num2)
   
 
    def get_result(self):
        return self.result
