from tkinter import *
from tkinter import ttk
import time

#count = 50
#ongoingText = "Scanned "
#Start = 'Start Scan'
#End = 'Cancel Scan'
#Time = 0.05

def script(count, ongoingText, Start, End, Time):
    gui=Tk()
    gui.title('Scan Files')
    gui.geometry('575x100')
    gui.configure(background='#3a3a3a')

    def StartProgress():
        interival = 100 / count
        gui.configure(background='#3a3a3a')
        for i in range(count):
            progress_var['value'] += interival
            stringvar.set(progress_var['value'])
            # get the value
            label.config(text=ongoingText+stringvar.get()+' %', bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10))
            # update value
            gui.update_idletasks()
            time.sleep(Time)
        gui.destroy()

    def StopProgress(ongoingText):
        # stop progress
        gui.configure(background='#3a3a3a')
        progress_var.stop()
        # set zero percent
        stringvar.set('00.0 %')
        label.config(text=ongoingText+stringvar.get(), bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10))
        

    # create an instance of progress bar

    progress_var=ttk.Progressbar(gui, orient="horizontal",
                    length=400, mode="determinate")
    progress_var.place(x=30,y=20)
    # set the value of progress bar
    stringvar=StringVar()
    stringvar.set('00.0 %')
    label=Label(gui,text=stringvar.get(), bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10))
    label.place(x=440,y=17)
    start_btn=Button(gui,text=Start,command=StartProgress, bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10))
    start_btn.place(x=30,y=50)
    gui.mainloop()
    pass

#script(count, ongoingText, Start, End, Time)