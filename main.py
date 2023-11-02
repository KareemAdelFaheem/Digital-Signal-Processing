from tkinter import *
import tkinter.font as font
import subprocess

# github testing 
class main_window:
    insta=0
    def __init__(self, windowroot):
        self.dialog = windowroot
        self.window.geometry("400x400")
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

        self.week1button.pack()
        self.week2button.pack()
        self.week3button.pack()
    

    def week1(self):
        subprocess.run(["python", "Week1/week1.py"], check=True)

    def week2(self):
        subprocess.run(["python", "Week2/week2.py"], check=True)

    def week3(self):
        subprocess.run(["python", "Week3/week3.py"], check=True)

def main():
    window = Tk()
    main_window(window)
    window.mainloop()

if __name__ == "__main__":
    main()
