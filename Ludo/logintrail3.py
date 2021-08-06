from tkinter import *
#import tkinter.messagebox as tkMessageBox
from tkinter import messagebox
import sqlite3
from tkinter import ttk
root = Tk()
root.title("ludo game login")
root.configure(background='skyblue')
#width = 1000
#height = 800
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
#x = (screen_width/2) - (width/2)
#y = (screen_height/2) - (height/2)
#photo = PhotoImage(file = "C:\Users\Pavan\Downloads\Ludo2DSimple PYTHON\Ludo2D-Game\ludo_full_big.jp")
#w = Label(root, image=photo)
#w.pack()
#root.geometry("%dx%d+%d+%d" % (width, height, x, y)
#root.resizable(0, 0)'''

#=======================================VARIABLES====================================
UserName = StringVar()
Password = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
CF       = StringVar()

#=======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_pavan.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `pavan` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT,cf TEXT)")
def home():
    global c
    c=Frame(root)
    c.pack()
    root.configure(background='skyblue')
    c.configure(background='skyblue')
    labTitle=Label(c,text="HOME",font=('arial',50,'bold'),fg='blue',bg='skyblue',bd=20)
    labTitle.grid(row=0,column=0,columnspan=2,pady=20)
    c1=Frame(c,width=800,height=400,bd=20,relief='flat')
    c1.grid(row=1,column=0)
    btnplay=Button(c1,text="PLAY",width=13,bg='pink',font=('arial',20,'bold'),command=imp)
    btnplay.grid(row=0,column=1)
    btnplay=Button(c1,text="HELP",width=13,bg='pink',font=('arial',20,'bold'),command=Help)
    btnplay.grid(row=1,column=1)
    btnplay=Button(c1,text="EXIT",width=13,bg='pink',font=('arial',20,'bold'),command=Exit)
    btnplay.grid(row=2,column=1)
    btnplay=Button(c1,text="LOGOUT",width=13,bg='pink',font=('arial',20,'bold'),command=logout)
    btnplay.grid(row=3,column=1)
def Help():
    c.destroy()
    global w
    w=Frame(root)
    w.pack(side=TOP)
    menubar = Menu(root)
    #filemenu = Menu(menubar, tearoff=0)
    #filemenu.add_command(command=LoginForm)
    menubar.add_cascade(label="<--", command=back1)
    root.config(menu=menubar)
    w1=Frame(w,width=800,height=300,bd=20,relief='ridge',bg='skyblue')
    w1.grid(row=1,column=0)
    lbl_lb1 = Label(w1, text="1.Unless you get a '6' when rolling the dice, your planes can't take off.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb1.grid(row=1,pady=2)
    lbl_lb2 = Label(w1, text="2.Press the ROLL button to roll the dice.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb2.grid(row=2,pady=2)
    lbl_lb3 = Label(w1, text="3.If it is a 6, then you can take another turn. So press ROLL again.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb3.grid(row=3,pady=2)
    lbl_lb4 = Label(w1, text="4.Click the plane which you want to move the first ROLL. The plane will move itself according to the number of the dice.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb4.grid(row=4,pady=2)
    lbl_lb5 = Label(w1, text="5.If the plane lands on stop, it cannot be killed.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb5.grid(row=5,pady=2)
    lbl_lb6 = Label(w1, text="6.To kill another color’s plane, you have to make your plane land on that box where other colored plane is.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb6.grid(row=6,pady=2)
    lbl_lb7 = Label(w1, text="7.If there are two planes of the same color on top of each other than that plane cannot be killed.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb7.grid(row=7,pady=2)
    lbl_lb8 = Label(w1, text="8.To win the game, your planes have to traverse around the board and come into the home lane.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb8.grid(row=8,pady=2)
    lbl_lb9 = Label(w1, text="9.If a player gets 3 six’s in a row, than his/her turn is void and next players plays.", font=('arial', 12), bd=18,bg='skyblue')
    lbl_lb9.grid(row=9,pady=2)
def logout():
    result = messagebox.askquestion('System', 'Are you sure you want to log out?', icon="warning")
    if result == 'yes':
        c.destroy()
        LoginForm()
    erase()
def imp():
    root.destroy()
    import Ludogame
def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
def back():
    RegisterFrame.destroy()
    LoginForm()
    erase()
def back1():
    w.destroy()
    home()
def erase():
    #btnManagement.config(state=DISABLE)
    #btnDoctor.config(state=DISABLE)
    #btnPatient.config(state=DISABLE)
    UserName.set("")
    Password.set("")
    #txtUserName.focus()
def Reset():
    UserName.set("")
    Password.set("")
    FIRSTNAME.set('')
    LASTNAME.set('')
    CF.set('')
def LoginForm():
    global LoginFrame
    LoginFrame = Frame(root)
    LoginFrame.pack()
    LoginFrame.configure(background='skyblue')
    LabelTitle=Label(LoginFrame,text="LUDO GAME",font=('arial',50,'bold'),fg='red',bg='skyblue',bd=20)
    LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
    Loginframe1=Frame(LoginFrame,width=800,height=300,bd=20,relief='flat',bg='skyblue')
    Loginframe1.grid(row=1,column=0)
    Loginframe2=Frame(LoginFrame,width=800,height=100,bd=20,relief='flat',bg='skyblue')
    Loginframe2.grid(row=2,column=0)
    Loginframe3=Frame(LoginFrame,width=800,height=200,bd=20,relief='flat',bg='skyblue')
    Loginframe3.grid(row=3,column=0,pady=2)
    lbl_username = Label(Loginframe1, text="Username:", font=('arial', 25), bd=18,bg='skyblue')
    lbl_username.grid(row=1,pady=2)
    lbl_password = Label(Loginframe1, text="Password:", font=('arial', 25), bd=18,bg='skyblue')
    lbl_password.grid(row=2,pady=2)
    #lbl_result1 = Label(Loginframe1, text="", font=('arial', 18))
    #lbl_result1.grid(row=3, columnspan=2)
    
    username = Entry(Loginframe1, font=('arial', 20), textvariable=UserName, width=15)
    username.grid(row=1, column=1)
    password = Entry(Loginframe1, font=('arial', 20), textvariable=Password, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(Loginframe2, text="Login", font=('arial', 20,'bold'), width=12,command=Login)
    btn_login.grid(row=0, column=0, pady=10)
    btnReset=Button(Loginframe2,text="Reset",width=13,font=('arial',20,'bold'),command=erase)
    btnReset.grid(row=0,column=1)

    #btnExit=Button(Loginframe2,text="Exit",width=12,font=('arial',20,'bold'),command=Exit)
    #btnExit.grid(row=0,column=3)
    lbl_register1 = Label(Loginframe3, text="Do Not Have An Account?", font=('arial', 12,'bold'),bg='skyblue')
    lbl_register1.grid(row=0, sticky=W)
    lbl_register = Label(Loginframe3, text="Sign Up", font=('arial', 16,'bold'),fg='blue',bg='skyblue')
    lbl_register.grid(row=0,column=1 )
    lbl_register.bind('<Button-1>', ToggleToRegister)

def RegisterForm():
    global RegisterFrame
    RegisterFrame = Frame(root)
    RegisterFrame.pack()
    RegisterFrame.configure(background='skyblue')
    menubar = Menu(root)
    #filemenu = Menu(menubar, tearoff=0)
    #filemenu.add_command(command=LoginForm)
    menubar.add_cascade(label="<--", command=back)
    root.config(menu=menubar)
    labTitle=Label(RegisterFrame,text="Sign Up",font=('arial',50,'bold'),fg='red',bd=20,bg='skyblue')
    labTitle.grid(row=0,column=0,columnspan=2,pady=20)
    
    Regframe1=Frame(RegisterFrame,width=800,height=400,bd=20,bg='skyblue',relief='flat')
    Regframe1.grid(row=1,column=1)
    Regframe2=Frame(RegisterFrame,width=800,height=100,bd=20,bg='skyblue',relief='flat')
    Regframe2.grid(row=2,column=1)
    
    lbl_username = Label(Regframe1, text="Username:", font=('arial', 18), bd=18,bg='skyblue')
    lbl_username.grid(row=3)
    lbl_password = Label(Regframe1, text="Password:", font=('arial', 18), bd=18,bg='skyblue')
    lbl_password.grid(row=4)
    lbl_firstname = Label(Regframe1, text="confirm password:", font=('arial', 18), bd=18,bg='skyblue')
    lbl_firstname.grid(row=5)
    lbl_firstname = Label(Regframe1, text="Firstname:", font=('arial', 18), bd=18,bg='skyblue')
    lbl_firstname.grid(row=1)
    lbl_lastname = Label(Regframe1, text="Lastname:", font=('arial', 18), bd=18,bg='skyblue')
    lbl_lastname.grid(row=2)
    
    #lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    #lbl_result2.grid(row=5, columnspan=2)
    username = Entry(Regframe1, font=('arial', 20), textvariable=UserName, width=15)
    username.grid(row=3, column=1)
    password = Entry(Regframe1, font=('arial', 20), textvariable=Password, width=15, show="*")
    password.grid(row=4, column=1)
    cf = Entry(Regframe1, font=('arial', 20), textvariable=CF, width=15, show="*")
    cf.grid(row=5, column=1)
    firstname = Entry(Regframe1, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=1, column=1)
    lastname = Entry(Regframe1, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=2, column=1)
    btn_login = Button(Regframe2, text="Register", font=('arial', 20,'bold'),width=13, command=Register)
    btn_login.grid(row=0, column=0, pady=20)
    bttnReset=Button(Regframe2,text="Reset",width=13,font=('arial',20,'bold'),command=Reset)
    bttnReset.grid(row=0,column=1)

def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def Register():
    Database()
    if UserName.get == "" or Password.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "" or CF.get()=='':
        messagebox.showinfo("LUDOGAME","please fill the following fields")
    else:
        cursor.execute("SELECT * FROM `pavan` WHERE `username` = ?", (UserName.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("LUDO GAME","UserName is already taken")
        elif Password.get()==CF.get():
            
            cursor.execute("INSERT INTO `pavan` (username, password, firstname, lastname, cf) VALUES(?, ?, ?, ?, ?)", (str(UserName.get()), str(Password.get()), str(FIRSTNAME.get()), str(LASTNAME.get()), CF.get()))
            conn.commit()
            answer=messagebox.showinfo("LUDO GAME","Account successfully created")  
            if(answer=='ok'):
                UserName.set("")
                Password.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                CF.set("")
                ToggleToLogin()
        else :
            messagebox.showinfo("LUDO GAME","enter same passwords")
        cursor.close()
        conn.close()
def Login():
    Database()
    if UserName.get == "" or Password.get() == "":
        messagebox.showerror("LUDO GAME","please complete the following fields")
    else:
        cursor.execute("SELECT * FROM `pavan` WHERE `username` = ? and `password` = ?", (UserName.get(), Password.get()))
        if cursor.fetchone() is not None:
            #messagebox.showinfo("LUDO GAME","Account successfully logged in")
            LoginFrame.destroy()
            #root.destroy()
            #from tkinter import Ludogame
            home()
        else:
            messagebox.showinfo("LUDO GAME","invalid username or password")
LoginForm()

#========================================MENUBAR WIDGETS==================================



#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.minsize(1350,750)
    root.mainloop()
   
