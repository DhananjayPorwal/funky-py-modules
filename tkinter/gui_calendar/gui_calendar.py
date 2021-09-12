import calendar
from tkinter import *
import tkinter


def showCalender():
    gui = Tk()
    gui.config(background='#d9dadb')
    gui.title("Calender for the year")
    gui.geometry("620x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()


if __name__ == '__main__':
    new = Tk()
    new.config(background='#d9dadb')
    new.title("Calender")
    new.geometry("167x180")
    cal = Label(new, text="Calender", bg='#d9dadb', font=("times", 28, "bold"))
    year = Label(new, text="Enter Year", bg='#d9dadb')
    year_field = Entry(new)
    Show = Button(new, text="Show Calender", fg="#0000D6",
                  bg="#d9dadb", command=showCalender)
    Exit = Button(new, text="Exit", fg="#0000D6", bg="#d9dadb", command=exit)

    cal.grid(row=1, column=1)
    year.grid(row=3, column=1)
    year_field.grid(row=6, column=1)
    Show.grid(row=8, column=1)
    Exit.grid(row=10, column=1)
    new.mainloop()
