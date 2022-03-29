from tkinter import *
import pandas as pd
import csv

win=Tk()

win.geometry("3000x3000")

canvas=Canvas(win, width=180, height=1800)
canvas.pack()

data = pd.read_csv('1.csv')
j = 0

with open('1.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for i, line in enumerate(reader):
        
        if i != 0:
            print(line, i)
            if(int(line[0]) < 1000 and int(line[1]) < 1000 and int(line[2]) < 1000):
                canvas.create_line(180 - int(line[0]), 180 - int(line[1]), 180 - int(line[0])+10, 180 - int(line[1]), fill="green", width=5)
                canvas.create_line(180 - int(line[0]), int(line[2])+180, 180 - int(line[0])+10, int(line[2])+180, fill="yellow", width=5)

win.mainloop()

