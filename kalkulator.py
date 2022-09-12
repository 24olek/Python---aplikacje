from ast import Try
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self ).__init__(master)
        self.grid()
        self.x = 0
        self.y = 0
        self.create_widgets()

    def create_widgets(self):
        self.x_label = Label(self, text = "Wprowadz pierwsza liczbe: ")
        self.x_label.grid(row = 0, column = 0, sticky = W)
        self.y_label = Label(self, text = "Wprowadz druga liczbe: ")
        self.y_label.grid(row = 1, column = 0, sticky = W)
        self.x = Entry(self)
        self.x.grid(row = 0, column = 1, sticky = W)
        self.y = Entry(self)
        self.y.grid(row = 1, column = 1, sticky = W)
        self.bttn1 = Button(self, width = 20, text = "Dodawanie", command = self.summary)
        self.bttn2 = Button(self, width = 20, text = "Odejmowanie", command = self.substraction)
        self.bttn3 = Button(self, width = 20, text = "Mnozenie", command = self.multiplition)
        self.bttn4 = Button(self, width = 20, text = "Dzielenie", command = self.dimension)
        self.bttn5 = Button(self, width = 20, text = "Potega", command = self.power)
        self.bttn6 = Button(self, width = 20, text = "Procent", command = self.percentage)
        self.bttn1.grid(row = 2, column = 0, sticky = W)
        self.bttn2.grid(row = 2, column = 1, sticky = W)
        self.bttn3.grid(row = 3, column = 0, sticky = W)
        self.bttn4.grid(row = 3, column = 1, sticky = W)
        self.bttn5.grid(row = 4, column = 0, sticky = W)
        self.bttn6.grid(row = 4, column = 1, sticky = W)
        self.result = Text(self, width = 40, height = 20, wrap = WORD)
        self.result.grid(row = 5, column = 0, columnspan = 2, sticky = W)

    def summary(self):
        try:
            result = int(self.x.get()) + int(self.y.get())
            self.result.delete(0.0, END)
            self.result.insert(0.0, result)
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")

    def substraction(self):
        try:
            result = int(self.x.get()) - int(self.y.get())
            self.result.delete(0.0, END)
            self.result.insert(0.0, result)
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")

    def multiplition(self):
        try:
            result = int(self.x.get()) * int(self.y.get())
            self.result.delete(0.0, END)
            self.result.insert(0.0, result)
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")

    def dimension(self):
        try:
            result = int(self.x.get()) / int(self.y.get())
            self.result.delete(0.0, END)
            self.result.insert(0.0, result)
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")

    def power(self):
        try:
            power = int(self.y.get()) - 1
            result = int(self.x.get())
            for i in range(power):
                result *= int(self.x.get())

            self.result.delete(0.0, END)
            self.result.insert(0.0, result)
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")

    def percentage(self):
        try:
            result = int(self.x.get()) / int(self.y.get()) * 100
            self.result.delete(0.0, END)
            self.result.insert(0.0, str(result) + "%")
        except:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "Error w kapitolu, kalkulator obsluguje jedynie liczby trollu")




root = Tk()
root.title("Kalkulator")
app = Application(root)


root.mainloop()


