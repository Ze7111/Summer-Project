try:
    from tkinter import *
    import time, random, threading
    from tkinter import ttk
    from core.loadingbar import script as loadingbar
    from modules.scanfiles import scancomp as scanfiles
    from modules.scanfiles import total as totallines
    from modules.fileviewer import FileWinodow as explorer
except:
    print("FAILED TO LOAD CORRECTLY")

def __init__():
# ---------------------- W I N D O W   C R E A T I O N ---------------------------------- 
    root = Tk()
    root.title("Dhruvans Notes Organizer")
    root.geometry('600x500')
    root.configure(background='#3a3a3a')
    
# ---------------------- S T Y L E ---------------------------------- 
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", troughcolor='#3a3a3a', bordercolor='#3a3a3a', background='white', lightcolor='white', darkcolor='white')
    
# ---------------------- H E A D I N G   B A R ---------------------------------- 
    Headding = Label(root, text = "Welcome To Dhruvans Notes Organizer", bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures SemiBold', 20))
    Headding.grid()
    
# ---------------------- S U B   H E A D I N G   B A R ---------------------------------- 
    subHeadding = Label(root, text = "Please Chose one of the options bellow", bg = '#3a3a3a', fg = 'white', font = ('Comic Code Ligatures Medium', 15))
    subHeadding.grid()

# ---------------------- B U T T O N   F U N C T I O N S ---------------------------------- 
    class refreshbuttonfunc():
        def refreshbtt():
            th = threading.Thread(target=refreshbuttonfunc.refreshsub)
            count = random.randint(10, 50)
            ongoingText = "Scanned "
            Start = 'Start Scan'
            End = 'Cancel Scan'
            Time = count / 1000
            scanfiles()
            th.start()
            loadingbar(count, ongoingText, Start, End, Time)
            th.join()
            
        def refreshsub():
            with open(r'databases\\allScanedFiles.dat', 'r') as fp:
                for count, line in enumerate(fp):
                    pass
            total = count - 2
            total = str(total)
            time.sleep(2)
            subHeadding.configure(text = total+" Files Scanned") # update the sub heading
        
    class compbuttonfunc():
        def compwindow():
            th = threading.Thread(target=compbuttonfunc.destroy)
            th.start()
            explorer('images\\--- Computing ---')
            
        def destroy():
            time.sleep(0.5)
            root.destroy()
        
        
    class mathbuttonfunc():
        def mathwindow():
            th = threading.Thread(target=compbuttonfunc.destroy)
            th.start()
            explorer('images\\--- Maths ---')
            
        def destroy():
            time.sleep(0.5)
            root.destroy()
        
    class physicsbuttonfunc():
        def physicswindow():
            th = threading.Thread(target=compbuttonfunc.destroy)
            th.start()
            explorer('images\\--- Physics ---')
            
        def destroy():
            time.sleep(0.5)
            root.destroy()
        
        
    class gamedesignbuttonfunc():
        def GDwindow():
            th = threading.Thread(target=compbuttonfunc.destroy)
            th.start()
            explorer('images\\--- Game Design ---')
            
        def destroy():
            time.sleep(0.5)
            root.destroy()



# ---------------------- B U T T O N   P L A C E M E N T S ---------------------------------- 
    bttRefresh = Button(root, text = "Refresh stored files" ,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), command=refreshbuttonfunc.refreshbtt, height = 2, width = 40)
    bttRefresh.grid(column=0, row=3, pady=10)
    
    bttComp = Button(root, text = "Open Computing files" ,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), command=compbuttonfunc.compwindow, height = 2, width = 40)
    bttComp.grid(column=0, row=5, pady=10)
    
    bttMath = Button(root, text = "Open Math files" ,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), command=mathbuttonfunc.mathwindow, height = 2, width = 40)
    bttMath.grid(column=0, row=7, pady=10)
    
    bttPhysics = Button(root, text = "Open Physics files" ,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), command=physicsbuttonfunc.physicswindow, height = 2, width = 40)
    bttPhysics.grid(column=0, row=9, pady=10)
    
    bttGD = Button(root, text = "Open Game Design files" ,bg = '#5a5a5a', fg = 'white', font = ('Comic Code Ligatures Medium', 10), command=gamedesignbuttonfunc.GDwindow, height = 2, width = 40)
    bttGD.grid(column=0, row=11, pady=10)
    
# ---------------------- M A I N   L O O P ---------------------------------- 
    root.mainloop()

__init__()