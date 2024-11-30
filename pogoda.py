import requests
import tkinter as tk
from tkinter import filedialog, messagebox

class Okno:
    def __init__(self, master):
        self.master = master
        master.title("Программа")
        master.geometry("400x300")

        # ввод 1
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        # ввод 2
        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # кнопка для выбора
        self.file_button = tk.Button(master, text="Выбрать файл", command=self.choose)
        self.file_button.pack()

        # Фрейм
        self.calc_frame = tk.Frame(master)
        self.calc_frame.pack(pady=10)

        # кнопка для сложения
        self.calc_button = tk.Button(self.calc_frame, text="Сложить числа", command=self.calc)
        self.calc_button.pack(side=tk.LEFT, padx=5) 

        # кнопка для вычитания
        self.subtract_button = tk.Button(self.calc_frame, text="Вычесть числа", command=self.subtract)
        self.subtract_button.pack(side=tk.LEFT, padx=5)

        # кнопка для погоды
        self.pogoda_button = tk.Button(master, text="Погода в Ульяновске", command=self.pogoda)
        self.pogoda_button.pack()

        #  для вывода
        self.resultViv = tk.Label(master, text="")
        self.resultViv.pack()

    def choose(self):  # для выбора файла
        file_path = filedialog.askopenfilename()  # открывает диалоговое окно
        if file_path:
            messagebox.showinfo("Выбранный файл", f"Выбран файл: {file_path}")

    def calc(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            result = num1 + num2
            self.resultViv.config(text=f"Результат сложения: {result}")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

    def subtract(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            result = num1 - num2
            self.resultViv.config(text=f"Результат вычитания: {result}")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

    def pogoda(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        qw = {'q': "Ульяновск", 'appid': "74d1b64251b951a1b9ca7e2dc0538761", 'units': 'metric'}
        try:
            otvet = requests.get(base_url, params=qw)
            otvet.raise_for_status()  # Проверка на ошибки HTTP
            data = otvet.json()
            temp = data['main']['temp']
            self.resultViv.config(text=f"Сейчас в Ульяновске: {temp}°C")
        except KeyError:
            messagebox.showerror("Ошибка, не удалось получить данные о температуре.")
        except:
            messagebox.showerror("Ошибка")

if __name__ == "__main__":
    root = tk.Tk()
    app = Okno(root)
    root.mainloop()