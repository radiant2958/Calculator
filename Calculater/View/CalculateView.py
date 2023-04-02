import tkinter as tk


from View.InterfaceView import InterfaceView




class CalculateView(InterfaceView):
    def __init__(self, controller, root):
        super().__init__()
        self.controller = controller
        InterfaceView.__init__(self)
        self.root = root
        self.root.title("Калькулятор")
      
        
       

        self.num1_label = tk.Label(self.root, text="введите первое число")
        self.num1_input=tk.Entry(self.root, width=25)
        self.num2_label = tk.Label(self.root, text="введите второе число")
        self.num2_input=tk.Entry(self.root, width=25)
        self.operation_label=tk.Label(self.root, text="введите оператора")
        self.operation_input=tk.Entry(self.root,width=25)
        self.result_label = tk.Label(self.root, text="Результат: ")
        self.button=tk.Button(self.root, text="РАВНО", command=self.calculate)

        self.num1_input.grid(row=0,column=0)
        self.num1_label.grid(row=1,column=0)
        self.operation_input.grid(row=0,column=1)
        self.operation_label.grid(row=1,column=1)
        self.num2_input.grid(row=0,column=2)
        self.num2_label.grid(row=1,column=2)
        self.button.grid(row=3,column=1)
        self.result_label.grid(row=4,column=0,columnspan=3)

    def calculate(self):
        try:
            num1 = float(self.num1_input.get())
            num2 = float(self.num2_input.get())
        except ValueError:
            self.update_result("Некорректный ввод")
            return

        operation = self.operation_input.get()
        try:
            self.controller.set_operation(operation)
            self.controller.calculate(num1, num2)
        except ValueError as e:
            self.update_result(str(e))
        else:
            self.update_result(str(self.controller.get_result()))
        

    def update_result(self, result):
            self.result_label.config(text="Результат: " + str(result))

    def clear_input(self):
            self.num1_input.delete(0, tk.END)
            self.num2_input.delete(0, tk.END)
            self.operation_input.delete(0, tk.END)


    def mainloop(self):
        self.root.mainloop()
        



