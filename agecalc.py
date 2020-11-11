import datetime
from tkinter import *
from tkinter import messagebox
import sqlite3

DB=sqlite3.connect('StoreThisPlease.sqlite3')
cursor=DB.cursor()
INDEX,E1,E2=0,None,None
query1='''
create table if not exists DOBS(
    id integer,
    birthday varchar(30),
    age varchar(30)
);
'''
query2='''
select count(*) from DOBS;
'''
cursor.execute(query1)
INDEX=tuple(cursor.execute(query2))[0][0]+1

def showLogs():
    global INDEX
    store=list(cursor.execute('select * from DOBS'))
    print(store)
    Display=Toplevel()
    Vbar=Scrollbar(Display)
    box=Listbox(Display,yscrollcommand=Vbar.set,width=50)
    Vbar.config(orient=VERTICAL,command=box.yview)
    box.insert(END,str(['Date of Birth',' Age ']))
    for i in store:
        i=list(i)
        del i[0]
        box.insert(END,str(i))
    Vbar.pack(side=RIGHT,fill=Y)
    box.pack(expand=True)
def setFullAge(y,m,d):
    global E2,E1,INDEX,DB
    fullDay.set(str(d))
    fullMonth.set(str(m))
    fullYear.set(str(y))
    if d!=0 and m!=0 and y!=0:
        E2=(str(y)+'y'+str(m)+'m'+str(d)+'d')
        cursor.execute('Insert into DOBS values ({},"{}","{}")'.format(INDEX,E1,E2))
        DB.commit()
        INDEX+=1
        E1,E2=None,None

def calculateAge():
    global E1
    currentdate = datetime.datetime.now()
    birthday = inputfield.get()
    try:
        birthdayDate=datetime.datetime.strptime(birthday,'%d-%m-%Y')
        E1=(birthday)
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
def on_closing():
    global DB
    DB.close()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Age Calculator")

canvas = Canvas(root,width = WIDTH, height = HEIGHT)
canvas.pack()

frame = Frame(root,bg="#ececec")
frame.place(relheight=1,relwidth=1,relx=0,rely=0)
history=Button(frame,command=lambda :showLogs(),text=' HISTORY ')
history.pack(side=RIGHT)

headingLabel = Label(frame,text="Y O U R . D E T A I L S",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel.pack(fill = X, expand =False, ipady = 18)

inputLabel = Label(frame,text="Date Of Birth (DD-MM-YYYY) :",font='AppleGothic 16',fg="#000000",bg="#ececec")
inputLabel.place(relheight=.05,relwidth=.55,relx=.06,rely=.22)

inputfield = StringVar()
myInput = Entry(frame,font = 'AppleGothic 16 italic',textvariable = inputfield,bg="#fcfcfc",fg="#000000")
myInput.place(relheight = .10,relwidth=.30,relx=.62,rely=.20)

calculateButton = Button(frame,text="Calculate Age",font = 'AppleGothic 16',bg="#ffffff",fg="red",activebackground="#ffffff",command=calculateAge)
calculateButton.place(relheight=.12,relwidth=.35,relx=.330,rely=.37)

headingLabel1 = Label(frame,text="Y O U R . A G E",bg="#ececec",fg="#000000",font='DecoType 24')
headingLabel1.place(relx=.30,rely=.52)

textAgeLabel=Label(frame,textvariable="fullAge",text="You are",bg="#ececec",fg="#000000",font='AppleGothic 16')
textAgeLabel.place(relheight=.05,relwidth=.15,relx=.1,rely=.70)


fullYear=StringVar()
fullYearOutput = Label(frame,textvariable =fullYear,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullYearOutput.place(relheight=.05,relwidth=.06,relx=.27,rely=.70)
fullYearText=Label(frame,text="Years",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullYearText.place(relheight=.05,relwidth=.1,relx=.34,rely=.70)


fullMonth=StringVar()
fullMonthOutput = Label(frame,textvariable =fullMonth,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullMonthOutput.place(relheight=.05,relwidth=.05,relx=.48,rely=.70)
fullMonthText=Label(frame,text="Months",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullMonthText.place(relheight=.05,relwidth=.13,relx=.55,rely=.70)


fullDay=StringVar()
fullDayOutput = Label(frame,textvariable =fullDay,bg="#ececec",fg="#000000",font='AppleGothic 16 bold')
fullDayOutput.place(relheight=.05,relwidth=.05,relx=.70,rely=.70)
fullDayText=Label(frame,text="Days",bg="#ececec",fg="#000000",font='AppleGothic 16')
fullDayText.place(relheight=.05,relwidth=.11,relx=.76,rely=.70)

setFullAge(0,0,0)

copyrightText = Label(frame,text = "Developed By Nishant",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText2=Label(frame,text="Teacher's Name : V. Devendran, Department : CSE, 2020",bg="#ececec",fg="#000000",font='AppleGothic 12')
copyrightText.place(relx=.09,rely=.85,relwidth=.8,relheight=.1)
copyrightText2.place(relx=.09,rely=.93,relwidth=.8,relheight=.05)

root.mainloop()
