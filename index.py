from  tkinter import*
class Register:
    def __init__(self,root):
       self.root=root
       self.root.title("Regiseration Window")
       self.root.geometry("1350x700+0+0")


root=Tk()
obj=Register(root)
root.mainloop()