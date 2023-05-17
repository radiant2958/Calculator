# Calculator  is a software project that represents a simple calculator for performing arithmetic operations. The project is implemented in Python using the tkinter library to create a graphical user interface.

The main functional capabilities of the calculator are:
performing basic arithmetic operations (+, -, *, /);
handling input errors (incorrect number input, attempting to divide by zero);
displaying the result of calculations on the screen.
The project has a modular structure consisting of three components:

Model - a module containing the abstract class AbstractModel, from which specific calculator implementations (Model) are inherited. The module also contains the abstract class Operation, from which specific arithmetic operation implementations are inherited.

Controller - a module containing the abstract class AbstractController, which defines the interface for managing the calculator. The concrete implementation of the management is carried out in the Controller class, which connects the Model and View.


View - a module containing the abstract class InterfaceView, from which specific implementations of the calculator's representation are inherited. 
In this project, a graphical representation is implemented in the CalculateView class, which uses the tkinter library to create a graphical user interface.

The project has a convenient interface that allows the user to easily perform arithmetic operations. The implementation of the calculator is modular, which makes it easy to expand its functionality in the future.

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"Калькулятор" - это программный проект, представляющий из себя простой калькулятор для выполнения арифметических операций. Проект реализован на языке Python с использованием библиотеки tkinter для создания графического интерфейса.

Основные функциональные возможности калькулятора:

выполнение базовых арифметических операций (+, -, *, /);
обработка ошибок ввода (некорректный ввод числа, попытка деления на ноль);
вывод результата вычислений на экран.
Проект представляет собой модульную структуру, состоящую из трех компонентов:

Model - модуль, содержащий абстрактный класс AbstractModel, от которого наследуются конкретные реализации калькулятора (Model). Модуль также содержит абстрактный класс Operation, от которого наследуются конкретные реализации арифметических операций.

Controller - модуль, содержащий абстрактный класс AbstractController, который определяет интерфейс для управления калькулятором. Конкретная реализация управления осуществляется в классе Controller, который связывает Model и View.

View - модуль, содержащий абстрактный класс InterfaceView, от которого наследуются конкретные реализации представления калькулятора. В данном проекте реализовано графическое представление в классе CalculateView, который использует библиотеку tkinter для создания графического интерфейса.

Проект имеет удобный интерфейс, позволяющий пользователю легко выполнять арифметические операции. Реализация калькулятора является модульной, что позволяет легко расширять его функциональность в будущем. 
