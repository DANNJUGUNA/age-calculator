from tkinter import *
from datetime import date

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("AGE CALCULATOR")

def calculateAge():
    today=date.today()
    birthdate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    Label(text=f"{nameValue.get()} your age is {age}",font=(('New Times Roman',10,'bold'))).place(x=300,y=500)

Label(text="Name", font=25).place(x=200
,y=250)
Label(text="Year_Of_Birth", font=25).place(x=200
,y=300)
Label(text="Month", font=25).place(x=200
,y=350)
Label(text="Day", font=25).place(x=200
,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,bd=3,font=('New Times Roman',15,'bold'))
nameEntry.place(x=350,y=250)

yearEntry=Entry(root,textvariable=yearValue,width=30,bd=3,font=('New Times Roman',15,'bold'))
yearEntry.place(x=350,y=300)

monthEntry=Entry(root,textvariable=monthValue,width=30,bd=3,font=('New Times Roman',15,'bold'))
monthEntry.place(x=350,y=350)
 
dayEntry=Entry(root,textvariable=dayValue,width=30,bd=3,font=('New Times Roman',15,'bold'))
dayEntry.place(x=350,y=400)

calageButton=Button(text="Calculate Age",font=('New Times Roman',10,'bold'),bg="blue",fg="white",width=11,height=1,command=calculateAge)
calageButton.place(x=350,y=450)


root.mainloop()

