from tkinter import *
import tkinter.font as font
import subprocess


class main_window:
    def __init__(self, windowroot):
        self.window = windowroot
        self.window.geometry("750x400")
        self.window.title("Digital Signal Processing")
        self.createWidgets()

    def createWidgets(self):
        buttonFont = font.Font(family='Helvetica', size=8, weight='bold')

        self.week1button = Button(
            self.window, text="WEEK #1", width="13", height="3", command=self.week1, font=buttonFont)
        self.week2button = Button(
            self.window, text="WEEK #2", width="13", height="3", command=self.week2, font=buttonFont)
        self.week3button = Button(
            self.window, text="WEEK #3", width="13", height="3", command=self.week3, font=buttonFont)
        self.week4button = Button(
            self.window, text="WEEK #4", width="13", height="3", command=self.week4, font=buttonFont)

        self.week1button.place(x=330, y=10)
        self.week2button.place(x=330, y=70)
        self.week3button.place(x=330, y=130)
        self.week4button.place(x=330, y=190)
    

    def week1(self):
        subprocess.run(["python", "Week1/week1.py"], check=True)

    def week2(self):
        subprocess.run(["python", "Week2/week2.py"], check=True)

    def week3(self):
        subprocess.run(["python", "Week3/week3.py"], check=True)

    def week4(self):
        subprocess.run(["python", "Week4/week4.py"], check=True)

def main():
    window = Tk()
    main_window(window)
    window.mainloop()

if __name__ == "__main__":
    main()
