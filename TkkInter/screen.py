import os
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Grid demo")
mainWindow.geometry("640x480-8+200")
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)
# Higher the weight- shrink and expand faster.
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)  # tkinetr.END =new item added at end, 0= reverse
listsScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listsScroll.grid(row=1, column=1, rowspan=2, sticky='nsw')
fileList['yscrollcommand'] = listsScroll.set

# Frame for radio button- LabelFrame let us add text and border is visible
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbvalue = tkinter.IntVar()  # when one option selected automatically another is deselected
rbvalue.set(2)

# Creating radio buttons
radioButton1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbvalue)
radioButton2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbvalue)
radioButton3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbvalue)
radioButton1.grid(row=0, column=0, sticky='w')
radioButton2.grid(row=1, column=0, sticky='w')
radioButton3.grid(row=2, column=0, sticky='w')

# Widget to display the result.
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for time spinner
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinner
hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

month = ("Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Aug", 'Sept', 'Oct', "Nov", "Dec")
# Date spinner
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# Date spinner
tkinter.Label(dateFrame, text='Day').grid(row=0, column=0)
tkinter.Label(dateFrame, text='Month').grid(row=0, column=1)
tkinter.Label(dateFrame, text='Year').grid(row=0, column=2)
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=30).grid(row=1, column=0)
monthSpin = tkinter.Spinbox(dateFrame, width=5, value=month).grid(row=1, column=1)
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2999).grid(row=1, column=2)

# Button OK & Cancel
okButton = tkinter.Button(mainWindow, text='OK', relief='sunken')
okButton.grid(row=4, column=3, sticky='e')
cancelButton = tkinter.Button(mainWindow, text='Cancel', relief='raised', command=mainWindow.destroy)
cancelButton.grid(row=4, column=4, sticky='w')


mainWindow.mainloop()
print(rbvalue.get())
