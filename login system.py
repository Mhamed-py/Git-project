from tkinter import*
from tkinter.font import BOLD
X=Tk()
X.geometry('500x500')
X.title('Login Administrator System')
X.config(background='#D5DBDB')
X.iconbitmap('C:\\Users\\mostafa\\Desktop\\login system\\ic.ico')
X.resizable(False,False)
#-------title----
title=Label(X,text='  Login to pngaaa Database  ',font=('courier',15,BOLD),bg='black',fg='white')
title.pack(fill='x')
#-------frame----
fr1=Frame(X,width='300',height='350',bg='whitesmoke')
fr1.pack(pady=30)
#-------photo----
photo=PhotoImage(file='C:\\Users\\mostafa\\Desktop\\login system\\login.png')
panel=Label(X,image=photo,bg='whitesmoke')
panel.place(x=180,y=70)
#-------LABLE----
lb1=Label(fr1,text='USERNAME:',font=('courier',15),bg='whitesmoke')
lb1.place(x=5,y=180)
lb1=Label(fr1,text='PASSWORD:',font=('courier',15),bg='whitesmoke')
lb1.place(x=5,y=230)
#--------ENTERY----
en1=Entry(fr1)
en1.place(x=130,y=186)
en2=Entry(fr1)
en2.place(x=130,y=235)
#-------button-----
bt1=Button(fr1,text='LOGIN',font=('courier',15),bg='#3498DB',width='25')
bt1.place(x=0,y=280)
X.mainloop()