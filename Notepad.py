from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def About():
    showinfo("Notepad","Notepad by BharathGT")

if __name__=='__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    #icon in notepad
    root.wm_iconbitmap("notes.ico")
    #screen size display
    root.geometry("743x434")

    #Add TextArea
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    #Lets create a menubar
    MenuBar = Menu(root)
    #Filemenu starts
    FileMenu = Menu(MenuBar,tearoff=0)

    #To open new file
    FileMenu.add_command(label="New",command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open",command=openFile)

    #To save the current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()

    #To exit from notepad
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #Filemenu ends

    #Edit menu Starts
    Editmenu = Menu(MenuBar,tearoff=0)

    #feature of cut
    Editmenu.add_command(label="Cut",command=cut)

    #feature of copy
    Editmenu.add_command(label="Copy", command=copy)

    # feature of paste
    Editmenu.add_command(label="Paste", command=paste)


    MenuBar.add_cascade(label="Edit",menu =Editmenu)
    # Edit menu ends

    #Help Menu Starts
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=About)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()

