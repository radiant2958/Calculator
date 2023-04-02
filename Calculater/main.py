
from View.CalculaterApp import CalculatorApp
from Controller.Controller import Controller


def main():
    controller = Controller()
    view = CalculatorApp(controller)
    view.run()

if __name__ == '__main__':
    main()