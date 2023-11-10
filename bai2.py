import tkinter

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


class CalculusTutor:

    def __init__(self):
        self.functions = []
        self.exercises = []
        self.solutions = []

        # Khởi tạo giao diện người dùng
        self.window = tkinter.Tk()
        self.label_function = tkinter.Label(self.window, text="Hàm số:")
        self.spinbox_function = tkinter.Spinbox(self.window, from_=0, to=len(self.functions) - 1)
        self.label_exercise = tkinter.Label(self.window, text="Bài tập:")
        self.spinbox_exercise = tkinter.Spinbox(self.window, from_=0, to=len(self.exercises) - 1)
        self.button_display = tkinter.Button(self.window, text="Hiển thị", command=self.display)
        self.button_solve = tkinter.Button(self.window, text="Giải", command=self.solve)

        # Sắp xếp các thành phần giao diện người dùng
        self.label_function.grid(row=0, column=0)
        self.spinbox_function.grid(row=0, column=1)
        self.label_exercise.grid(row=1, column=0)
        self.spinbox_exercise.grid(row=1, column=1)
        self.button_display.grid(row=2, column=0)
        self.button_solve.grid(row=2, column=1)

        # Bắt đầu vòng lặp sự kiện
        self.window.mainloop()

    def add_function(self, function):
        self.functions.append(function)

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def add_solution(self, solution):
        self.solutions.append(solution)

    def display_function(self):
        function = self.functions[self.spinbox_function.get()]
        print(f"Hàm số số: {function}")
        print(f"Đồ thị hàm số:")
        plt.plot(function)
        plt.show()

        # Hiển thị đồ thị hàm số trên giao diện Tinker
        leds = np.array(function(np.linspace(-5, 5, 64)) * 255).astype(np.uint8)
        self.display.set_leds(leds)
        self.display.write()

    def display_exercise(self):
        exercise = self.exercises[self.spinbox_exercise.get()]
        print(f"Bài tập: {exercise}")
        print(f"Giải: {self.solutions[self.spinbox_exercise.get()]}")

        # Hiển thị bài tập và giải trên giao diện Tinker
        leds = np.array(exercise).astype(np.uint8)
        self.display.set_leds(leds)
        self.display.write()

    def solve(self):
        exercise = self.exercises[self.spinbox_exercise.get()]
        solution = self.solutions[self.spinbox_exercise.get()]
        print(f"Giải bài tập: {solution}")

        # Hiển thị kết quả giải trên giao diện Tinker
        leds = np.array(solution).astype(np.uint8)
        self.display.set_leds(leds)
        self.display.write()


def main():
    tutor = CalculusTutor()

    # Thêm các hàm số

    tutor.add_function(lambda x: x ** 2)
    tutor.add_function(lambda x: np.sin(x))
    tutor.add_function(lambda x: np.exp(x))

    # Thêm các bài tập
  tutor.add_exercise(lambda: integrate.quad(lambda x: x ** 2, 0, 1))
    tutor.add_exercise(lambda: np.sin(np.pi/2))
    # Thêm các giải

    tutor.add_solution(1.0)
    tutor.add_solution(1)
    tutor.add_solution(np.inf)

    # Hiển thị giao diện người dùng

    tutor.window.mainloop()
