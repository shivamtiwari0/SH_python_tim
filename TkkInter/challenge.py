try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480")
mainWindow['padx'] = 8

# Setting up result menu
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='w')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='we')
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1000)

keys = [['C', 'CE'],
        ['7', '8', '9', '+'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '*'],
        ['0', '=', '/'], ]

row = 0
for key in keys:
    col = 0
    for buts in key:
        if buts == '=':
            columnspan = 2
        else:
            columnspan = 1
        a = tkinter.Button(keyPad, text=buts)
        a.grid(row=row, column=col, columnspan=columnspan, sticky='we')
        col += columnspan
    row += 1

keyPad['padx'] = 8
mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + 8, keyPad.winfo_height() + result.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 8, keyPad.winfo_height() + result.winfo_height())

mainWindow.mainloop()
