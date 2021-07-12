import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480-8+200")  # 640 is width, 480 height, 8 pixel from most left of screen , 200 from top

label = tkinter.Label(mainWindow, text="Hello World, I'm here.")
label.grid(row=0, column=0)

leftframe = tkinter.Frame(mainWindow)
leftframe.grid(row=1, column=1)

canvas = tkinter.Canvas(leftframe)
# canvas.pack(side='left', fill=tkinter.X, expand=True)  # fill =tkinter.X or Y or BOTH sometimes without defining
# expand fill doesn't work
canvas.grid(row=0, column=1)

rightframe = tkinter.Frame(mainWindow)
rightframe.grid(row=1, column=2)

button1 = tkinter.Button(rightframe, text='button1')
button2 = tkinter.Button(rightframe, text='button2')
button3 = tkinter.Button(rightframe, text='button3')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0, sticky='nsew')
button3.grid(row=2, column=0)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

leftframe.config(relief='sunken', borderwidth=1)
rightframe.config(relief='sunken', borderwidth=1)
rightframe.grid(sticky='new')
leftframe.grid(sticky='ns')

rightframe.columnconfigure(0, weight=1)
button2.grid(sticky='we')

mainWindow.mainloop()
