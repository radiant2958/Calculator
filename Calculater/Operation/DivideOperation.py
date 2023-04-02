from Operation.Operation import Operation


class DivideOperation(Operation):
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")
        return num1 / num2