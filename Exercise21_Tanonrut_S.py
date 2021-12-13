from tkinter import *
import math

def leftClickButton(event):
    bodyRatio = float(writeWeightEntry.get())/math.pow(float(writeHeightEntry.get())/100, 2)
    resultLabel.configure(text=bodyRatio)
    if bodyRatio >= 30:
        Label(mainWindow, text = "You are very fat.").grid(row=3, column=2)
    elif bodyRatio >= 29.99 and bodyRatio >= 25:
        Label(mainWindow, text="You are fat.").grid(row=3, column=2)
    elif bodyRatio >= 24.99 and bodyRatio >= 23:
        Label(mainWindow, text="You are overweight.").grid(row=3, column=2)
    elif bodyRatio >= 22.99 and bodyRatio >= 18.6:
        Label(mainWindow, text="You are the right weight.").grid(row=3, column=2)
    else:
        Label(mainWindow, text="You are too skinny.").grid(row=3, column=2)



mainWindow = Tk()
mainWindow.title('Body Ratio')

writeWeightLaber = Label(mainWindow, text="Your weight (Kg)")
writeWeightLaber.grid(row=0, column=1)
writeWeightEntry = Entry(mainWindow)
writeWeightEntry.grid(row=0, column=2)
writeHeightLabel = Label(mainWindow, text="Your height (cm)")
writeHeightLabel.grid(row=1, column=1)
writeHeightEntry = Entry(mainWindow)
writeHeightEntry.grid(row=1, column=2)
calculateButtom = Button(mainWindow, text="Calculate")
calculateButtom.bind('<Button-1>', leftClickButton)
calculateButtom.grid(row=2, column=1)
resultLabel = Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2)

mainWindow.geometry("300x300")
mainWindow.mainloop()