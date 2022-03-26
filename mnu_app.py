# A python program to create a menubar and adding
# File and Edit menus with some options
from tkinter import *
from tkinter import filedialog


class MyMenuDemo:
    def __init__(self, root):
        # create menubar
        self.menubar = Menu(root)

        # attach the menubar to root window
        root.config(menu=self.menubar)

        # create Menu File
        self.filemenu = Menu(root, tearoff=0)

        # create menuitem in filemenu
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command=self.savefile)

        # add a horizontal line as a seperator
        self.filemenu.add_separator()

        # create menuitem Exit in filemenu
        self.filemenu.add_command(label="Exit", command=root.destroy)

        # add the edit menu with a name Edit to the menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create Menu Edit
        self.editmenu = Menu(root, tearoff=0)

        # create menuitem in filemenu
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)

        # add the edit menu with a name Edit to the menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    def donothing(self):
        print("You clicked")

    def openfile(self):
        self.filename = filedialog.askopenfilename(parent=root, title="select a file", \
                                                   filetypes=(("Python files", "*.py"), \
                                                              ("All files", "*.*")))
        if self.filename != None:
            f1 = open(self.filename, "r")
            # read the content of file
            c = f1.read()
            # create a text box and add it to root window
            self.t = Text(root, width=80, height=20, wrap=WORD)
            self.t.pack()
            self.t.insert(1.0, c)
            f1.close()

    def savefile(self):
        self.filemenu = filedialog.asksaveasfilename(parent=root, defaultextension=".txt")
        if self.filename != None:
            f2 = open(self.filename, 'w')
            c = str(self.t.get(1.0, END))
            f2.write(c)
            f2.close()


root = Tk()
root.title("Menu Example")
obj = MyMenuDemo(root)
root.geometry("700x500")
root.mainloop()