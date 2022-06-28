# ---------------------- L O A D   L I B A R I E S / F I L E S ----------------------------------
try:
    import linecache, os, ctypes, pathlib, random, threading, time, string, sys, shutil
    from tkinter import *
    from tkinter import filedialog, ttk
except:
    print("FAILED TO LOAD CORRECTLY {f i l e   v i e w e r}")

# ---------------------- I N A T I L I Z E ---------------------------------- 
def FileWinodow(mainpath):
    
    # ---------------------- W I N D O W   C R E A T I O N ----------------------------------
    # Increase Dots Per inch so it looks sharper
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    root = Tk()
    # set a title for file explorer main window
    root.title('Compputing Notes')
    root.geometry("575x450")
    root.configure(background='#3a3a3a')
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)
        
# ---------------------- C H A N G E   D I R ----------------------------------         
    def pathChange(*event):
        # Get all Files and Folders from the given Directory
        directory = os.listdir(currentPath.get())
        # Clearing the list
        list.delete(0, END)
        # Inserting the files and directories into the list
        for file in directory:
            list.insert(0, file)

# ---------------------- C H A N G E   D I R   B Y   C L I C K I N G ---------------------------------- 
    def changePathByClick(event=None):
        # Get clicked item.
        picked = list.get(list.curselection()[0])
        # get the complete path by joining the current path with the picked item
        path = os.path.join(currentPath.get(), picked)
        # Check if item is file, then open it
        if os.path.isfile(path):
            print('Opening: '+path)
            os.startfile(path)
        # Set new path, will trigger pathChange function.
        else:
            currentPath.set(path)

# ---------------------- C R E A T E   N E W    F I L E    F U N C T I O N ---------------------------------- 
    def open_popup():
        global top
        top = Toplevel(root)
        top.geometry("250x150")
        top.resizable(False, False)
        top.title("New File or Folder")
        top.configure(background='#3a3a3a')
        top.columnconfigure(0, weight=1)
        Label(top, text='Enter File or Folder name',bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10)).grid()
        Entry(top,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), textvariable=newFileName).grid(column=0, pady=10)
        Button(top, text="Create", command=newFileOrFolder,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10)).grid(pady=10)
    
    # ---------------------- C R E A T E   N E W    F I L E  ---------------------------------- 
    def newFileOrFolder():
        # check if it is a file name or a folder
        if len(newFileName.get().split('.')) != 1:
            open(os.path.join(currentPath.get(), newFileName.get()), 'w').close()
        else:
            os.mkdir(os.path.join(currentPath.get(), newFileName.get()))
        # destroy the top
        top.destroy()
        pathChange()

    top = ''

# ---------------------- A L L   B U T T O N S   A N D   O T H E R    V I S I B L E    I T E M S ---------------------------------- 
    # String variables
    newFileName = StringVar(root, "example.txt", 'new_name')
    currentPath = StringVar(root, name='currentPath', value=mainpath)
    # Bind changes in this variable to the pathChange function
    currentPath.trace('w', pathChange)

    Entry(root, textvariable=currentPath,bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10)).grid(sticky='NSEW', pady=10)
    

    # List of files and folder
    list = Listbox(root,bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 10))
    list.grid(sticky='NSEW', column=0, row=1, ipady=10, ipadx=200)

    # List Accelerators
    list.bind('<Double-1>', changePathByClick)
    list.bind('<Return>', changePathByClick)

    # Menu
    menubar = Menu(root, background='#3a3a3a', fg='white')
    # Adding a new File button
    menubar.add_command(label="Add File or Folder", command=open_popup)
    # Adding a quit button to the Menubar
    menubar.add_command(label="Quit", command=root.quit)
    # Make the menubar the Main Menu
    root.config(menu=menubar)

    # Call the function so the list displays
    pathChange('')
    
# ---------------------- M A I N   L O O P ---------------------------------- 
    root.mainloop()
    
