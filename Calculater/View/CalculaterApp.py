import tkinter as tk

from View.CalculateView import CalculateView
from Controller.Controller import Controller
from Controller.AbstractController import AbstractController

class CalculatorApp:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.view = CalculateView(self.controller, self.root)

    def run(self):
        self.view.mainloop()


if __name__ == '__main__':
    controller = Controller()
    app = CalculatorApp(controller)
    app.run()
