from tkinter import *
root = Tk()

root.resizable(width=False, height=False)  # The window size of the game.
root.geometry('1000x750')
root.configure(background='skyblue')
root.title("winner")
global c
c=Frame(root)
c.pack()
#root.configure(background='skyblue')
c.configure(background='skyblue')
labTitle=Label(c,text="blue team wins",font=('arial',50,'bold'),fg='blue',bg='skyblue',bd=20)
labTitle.grid(row=0,column=0,columnspan=2,pady=20)
root.minsize(1350,750)
root.mainloop()
