import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+8+200")  # 640 is width, 480 height, 8 pixle from most left of screen , 200 from top

label = tkinter.Label(mainWindow, text="Hello World, I'm here.")
label.pack(side='top')

leftframe = tkinter.Frame(mainWindow, bd=1, relief='raised')
leftframe.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftframe, borderwidth=1, relief='raised')
# canvas.pack(side='left', fill=tkinter.X, expand=True)  # fill =tkinter.X or Y or BOTH sometimes without defining
# expand fill doesn't work
canvas.pack(side='left', anchor='n')

rightframe = tkinter.Frame(mainWindow, bd=1, relief='raised')
rightframe.pack(side='right', anchor='n', fill=tkinter.X, expand=True)

button1 = tkinter.Button(rightframe, text='button1')
button2 = tkinter.Button(rightframe, text='button2')
button3 = tkinter.Button(rightframe, text='button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()