import datetime
from tkinter import *
from tkinter import messagebox

def setFullAge(y,m,d):
    fullDay.set(str(d))
    fullMonth.set(str(m))
    fullYear.set(str(y))

def calculateAge():
    currentdate = datetime.datetime.now()
    birthday = inputfield.get()
    try:
        birthdayDate=datetime.datetime.strptime(birthday,'%d-%m-%Y')
    except:
        setFullAge(0,0,0)
        messagebox.showerror("Error","Wrong Value of Birthday")
        return
    nextBirthday = str(birthdayDate.day)+'-'+str(birthdayDate.month)+'-'+str(currentdate.year+1)
    nextBirthdayDate=datetime.datetime.strptime(nextBirthday,'%d-%m-%Y')

    years = (currentdate-birthdayDate).total_seconds()/3600/24/365.242
    yearsInt = int(years)

    months = (years-yearsInt)*12
    monthsInt = int(months)

    days = (months-monthsInt)*(365.242/12)
    daysInt = int(days)

    setFullAge(yearsInt,monthsInt,daysInt)

HEIGHT = 350
WIDTH = 600

root = Tk()
root.title("Age Calculator")

canvas = Canvas(root,width = WIDTH, height = HEIGHT)
canvas.pack()

frame = Frame(root,bg="#ececec")
frame.place(relheight=1,relwidth=1,relx=0,rely=0)

headingLabel = Label(frame,text="Your Details",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel.pack(fill = X, expand =False, ipady = 18)

inputLabel = Label(frame,text="Date Of Birth (DD-MM-YYYY) :",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel.place(relheight=.05,relwidth=.55,relx=.06,rely=.22)

inputfield = StringVar()
myInput = Entry(frame,font = 'AppleGothic 16 italic',textvariable = inputfield,bg="#fcfcfc",fg="#000000")
myInput.place(relheight = .10,relwidth=.30,relx=.62,rely=.20)

calculateButton = Button(frame,text="Calculate Age",font = 'AppleGothic 16',bg="#ffffff",fg="red",activebackground="#ffffff",command=calculateAge)
calculateButton.place(relheight=.12,relwidth=.35,relx=.375,rely=.37)

headingLabel1 = Label(frame,text="Your Age",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel1.place(relx=.41,rely=.52)

textAgeLabel=Label(frame,textvariable="fullAge",text="You are",bg="#ececec",fg="#000000",font='AppleGothic 16')
textAgeLabel.place(relheight=.05,relwidth=.15,relx=.1,rely=.70)


fullYear=StringVar()
fullYearOutput = Label(frame,textvariable =fullYear,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullYearOutput.place(relheight=.05,relwidth=.06,relx=.27,rely=.70)
fullYearText=Label(frame,text="Years",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullYearText.place(relheight=.05,relwidth=.1,relx=.35,rely=.70)


fullMonth=StringVar()
fullMonthOutput = Label(frame,textvariable =fullMonth,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullMonthOutput.place(relheight=.05,relwidth=.05,relx=.48,rely=.70)
fullMonthText=Label(frame,text="Months",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullMonthText.place(relheight=.05,relwidth=.13,relx=.56,rely=.70)


fullDay=StringVar()
fullDayOutput = Label(frame,textvariable =fullDay,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullDayOutput.place(relheight=.05,relwidth=.05,relx=.70,rely=.70)
fullDayText=Label(frame,text="Days",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullDayText.place(relheight=.05,relwidth=.15,relx=.76,rely=.70)
#set default value
setFullAge(0,0,0)


copyrightText = Label(frame,text = "Developed By Nishant",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText2=Label(frame,text="Teacher's Name : V. Devendran, Department : CSE, 2020",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText.place(relx=.09,rely=.85,relwidth=.8,relheight=.1)
copyrightText2.place(relx=.09,rely=.93,relwidth=.8,relheight=.05)


root.mainloop()
