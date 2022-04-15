import json
from tkinter import *
import random               # For random Questions
def quiz_page_science():
    global ques
    global quizpage,indexes,answers,user_answer
    login_page.destroy()
    user_page.destroy()
    quizpage = Tk()
    quizpage.title("Science Quiz")
    quizpage.geometry("1600x1400")
    bg = PhotoImage(file="quiz1.png")
    label1 = Label(quizpage, image=bg)
    label1.place(x=0, y=0)
    # load questions and answer choices from json file
    with open('question.json', encoding="utf8") as f:
        data = json.load(f)
    # lists of questions and answers_choice
    questions = [v for v in data[0].values()]
    answers_choice = [v for v in data[1].values()]
    answers=[2,1,0,2,0,0,2,1,1,0]
    user_answer = []
    indexes = []
    def gen():
        global indexes
        while (len(indexes) < 10):
            x = random.randint(0, 9)
            if x in indexes:
                continue
            else:
                indexes.append(x)
    def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        labelresulttext = Label(
            quizpage,
            font=("Consolas", 20),
            background="black",)
        labelresulttext.pack(pady=20)
        if score >= 20:
            labelresulttext.configure(text="You Are Excellent !!",background="black",foreground="green")
        elif (score >= 10 and score < 20):
            labelresulttext.configure(text="You Can Be Better !!",background="black",foreground="white")
        else:
            labelresulttext.configure(text="You Should Work Hard !!",background="black",foreground="white")
        labeltext = Label(
            quizpage,
            text=f"Your Score is \"{score}\" out of \"50\" \n\n Percentage is \"{(score/50)*100}\" \n \n Thanks For playing !! " ,
            font=("LCDMono2", 24, "bold"),
            background="black",foreground="white")
        labeltext.pack(pady= 200)
    def calc():
        global indexes, user_answer, answers
        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                score = score + 5
            x += 1
        showresult(score)
    ques = 1
    def selected():
        global radiovar, user_answer,lblQuestion, r1, r2, r3
        global ques
        x = radiovar.get()
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 10:
            lblQuestion.config(text=questions[indexes[ques]])
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            ques += 1
        else:
            calc()
    def startquiz():
        global lblQuestion, r1, r2, r3
        lblQuestion = Label(
            quizpage,
            text=questions[indexes[0]],
            font=("Times", 16),
            justify="center",
            foreground="white",
            wraplength=400,
            background="black",)
        lblQuestion.pack(pady=(300, 30))
        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)
        r1 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][0],
            font=("Times", 12),
            value=0,
            variable=radiovar,
            command=selected,
            foreground="white",
            background="black",)
        r1.pack(pady=5)
        r2 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][1],
            font=("Times", 12),
            value=1,
            variable=radiovar,
            command=selected,
            foreground="white",
            background="black",)
        r2.pack(pady=5)
        r3 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][2],
            font=("Times", 12),
            value=2,

            variable=radiovar,
            command=selected,
            foreground="white",
            background="black",)
        r3.pack(pady=5)
    def startIspressed():
        lblInstruction.destroy()
        lblRules.destroy()
        btnStart.destroy()
        gen()
        startquiz()
    btnStart = Button(
        quizpage,
        text="START QUIZ",
        font="LCDMono2 40 bold", borderwidth=10
        , relief=GROOVE, background="light green",
        command=startIspressed,)
    btnStart.pack(pady=110)
    lblInstruction = Label(
        quizpage,
        text="Read The Rules And\nClick Start Once You Are ready",
        background="black",
        foreground="white",
        font=("Consolas", 14),
        justify="center",)
    lblInstruction.pack(pady=10)
    lblRules = Label(
        quizpage,
        text="This quiz contains 10 questions\nOnce you select a option it wil be your final choice\nhence think before you select\n This GUI have less features than our main CLI Project File ",
        width=100,
        font=("Times", 20),
        background="#000000",
        foreground="#FACA2F",)
    lblRules.pack(pady=50
                  , side=BOTTOM)
    quizpage.mainloop()

def quiz_page_gk():
    global ques
    global quizpage,indexes,answers,user_answer
    login_page.destroy()
    user_page.destroy()
    quizpage = Tk()
    quizpage.title("GK Quiz")
    quizpage.geometry("1400x1200")
    bg = PhotoImage(file="quiz1.png")
    label1 = Label(quizpage, image=bg)
    label1.place(x=0, y=0)
    # load questions and answer choices from json file
    with open('gk question.json', encoding="utf8") as f:
        data = json.load(f)
    # lists of questions and answers_choice
    questions = [v for v in data[0].values()]
    answers_choice = [v for v in data[1].values()]
    answers=[2,0,2,2,1,0,2,0,0,1]
    user_answer = []
    indexes = []
    def gen():
        global indexes
        while (len(indexes) < 10):
            x = random.randint(0, 9)
            if x in indexes:
                continue
            else:
                indexes.append(x)
    def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        labelresulttext = Label(
            quizpage,
            font=("Consolas", 20),
            background="black",foreground="white")
        labelresulttext.pack(pady=20)
        if score >= 20:
            labelresulttext.configure(text="You Are Excellent !!",background="black",foreground="green")
        elif (score >= 10 and score < 20):
            labelresulttext.configure(text="You Can Be Better !!",background="black",foreground="white")
        else:
            labelresulttext.configure(text="You Should Work Hard !!",background="black",foreground="white")
        labeltext = Label(
            quizpage,
            text=f"\nYour Score is \"{score}\" out of \"50\" \n\n Percentage is \"{(score/50)*100}\" \n \n Thanks For playing !! " ,
            font=("LCDMono2", 24, "bold"),
            background="black",
            foreground="white")
        labeltext.pack(pady=200)
    def calc():
        global indexes, user_answer, answers
        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                score = score + 5
            x += 1
        showresult(score)
    ques = 1
    def selected():
        global radiovar, user_answer,lblQuestion, r1, r2, r3
        global ques
        x = radiovar.get()
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 10:
            lblQuestion.config(text=questions[indexes[ques]])
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            ques += 1
        else:
            calc()
    def startquiz():
        global lblQuestion, r1, r2, r3
        lblQuestion = Label(
            quizpage,
            text=questions[indexes[0]],
            font=("Times", 16),
            justify="center",
            wraplength=400,
            background="black",
            foreground="white")
        lblQuestion.pack(pady=200)
        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)
        r1 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][0],
            font=("Times", 12),
            value=0,
            variable=radiovar,
            command=selected,
            background="black",
            foreground="white")
        r1.pack(pady=5)
        r2 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][1],
            font=("Times", 12),
            value=1,
            variable=radiovar,
            command=selected,
            background="black",
            foreground="white")
        r2.pack(pady=5)
        r3 = Radiobutton(
            quizpage,
            text=answers_choice[indexes[0]][2],
            font=("Times", 12),
            value=2,
            variable=radiovar,
            command=selected,
            background="black",
            foreground="white")
        r3.pack(pady=5)
    def startIspressed():
        lblInstruction.destroy()
        lblRules.destroy()
        btnStart.destroy()
        gen()
        startquiz()
    btnStart = Button(
        quizpage,
        text="START QUIZ",
        font="LCDMono2 40 bold", borderwidth=10
        , relief=GROOVE, background="light green",
        command=startIspressed,)
    btnStart.pack(pady=110)
    lblInstruction = Label(
        quizpage,
        text="Read The Rules And\nClick Start Once You Are ready",
        background="black",
        foreground="white",
        font=("Consolas", 14),
        justify="center",)
    lblInstruction.pack(pady=10)
    lblRules = Label(
        quizpage,
        text="This quiz contains 10 questions\nOnce you select a option it wil be your final choice\nhence think before you select\n This GUI have less features than our main CLI Project File ",
        width=100,
        font=("Times", 20),
        background="#000000",
        foreground="#FACA2F",)
    lblRules.pack(pady=50
                  , side=BOTTOM)
    quizpage.mainloop()
def test():
    test_page=Tk()
    test_page.title("QUIZ")
    test_page.geometry("1200x1200")
    test_page.config(background="white")
    Label(test_page,text="~| WELCOME TO OUR QUIZ APPLICATION |~",
          font="AgencyFB 40 bold",
          background="white",).pack()
    Label(test_page, text="Select A knowledge Area ",
          font="AgencyFB 20 bold",
          background="white", ).pack()
    science_easy=Button(test_page,
                        text="SCIENCE",
                        font="LCDMono2 20 bold",
                        borderwidth=10
                        ,relief=GROOVE,
                        background="light blue",
                        command=quiz_page_science)
    science_easy.pack(anchor="n",ipady=15,pady=5)
    gk = Button(test_page,
                          text="GENERAL KNOWLEDGE",
                          font="LCDMono2 20 bold",
                          borderwidth=10
                          , relief=GROOVE,
                          background="light blue",
                          command=quiz_page_gk)
    gk.pack(anchor="n", ipady=15, pady=5)
    test_page.mainloop()
def check():
    with open("user_details.txt", "r") as f:
        if userentrylogin.get()+","+passentrylogin.get() + "\n" in f.readlines():
            test()
        else:
            Label(login_page,text="INVALID USERNAME OR PASSWORD | TRY AGAIN", font="TimesNewRoman 30 bold").pack()
def login():
    global userentrylogin, passentrylogin, login_page
    login_page = Tk()
    login_page.title("LOGIN")
    login_page.geometry("1200x1000")
    login_page.config(background="white")
    Label(login_page, text="ENTER USER NAME AND PASSWORD TO LOGIN",
          font="stencil 20 bold",
          background="white").pack(pady=30)
    uservalue = StringVar()
    passvalue = StringVar()
    userentrylogin = Entry(login_page,
                           font="TimesNewRoman 20 bold",
                           border=2,
                           relief=SOLID,
                           textvariable=uservalue)
    passentrylogin = Entry(login_page,
                           font="TimesNewRoman 20 bold",
                           border=2,
                           relief=SOLID,
                           textvariable=passvalue)
    Label(login_page,
          font="TimesNewRoman 20 bold",
          background="white", border=10, text="Username: ").pack()
    userentrylogin.pack(pady=20)  # .grid(row=0, column=1)
    Label(login_page,
          font="TimesNewRoman 20 bold",
          background="white",
          text="Password").pack(pady=20)
    passentrylogin.pack()  # .grid(row=1, column=1)
    Button(login_page, text="Login",font="LCDMono2 20 bold",borderwidth=10
                        ,relief=GROOVE,background="light blue", command=check).pack(pady=40)  # command=getvals).grid()
    login_page.mainloop()
def register():
    register_page = Tk()
    register_page.title("REGISTRATION")
    register_page.geometry("1200x1000")
    register_page.config(background="white")
    Label(register_page, text="ENTER USER NAME AND PASSWORD TO REGISTER TO OUR PORTAL",
          font="stencil 20 bold",
          background="white").pack(pady=30)
    def write():
        with open("user_details.txt", "a") as f:
            f.write(str(userentry.get()) + "," + str(passentry.get())+"\n")
        register_page.destroy()
        Label(user_page,text="YOU HAVE SUCCESSFULLY REGISTERED",font="Roboto 30 bold",background="blue",foreground="light green").pack()
    userentry = Entry(register_page,
                      font="TimesNewRoman 20 bold",
                      border=2,
                      relief=SOLID)
    passentry = Entry(register_page,
                      font="TimesNewRoman 20 bold",
                      border=2,
                      relief=SOLID)
    Label(register_page,
          font="TimesNewRoman 20 bold",
          background="white", border=10, text="Username: ").pack()
    userentry.pack(pady=20)  # .grid(row=0, column=1)
    Label(register_page,
          font="TimesNewRoman 20 bold",
          background="white",
          text="Password").pack()
    passentry.pack(pady=20)  # .grid(row=1, column=1)
    Button(register_page, text="Register",font="LCDMono2 20 bold",borderwidth=10
                        ,relief=GROOVE,background="light blue", command=write).pack()  # command=getvals).grid()
    register_page.mainloop()
def user():
    global user_page
    first_page.destroy()
    user_page = Tk()
    user_page.title("Login or register")
    user_page.geometry("1400x1000")
    bg = PhotoImage( file = "loginbg.png")
    log = PhotoImage(file="login.png")
    label1 = Label(user_page, image=bg)
    label1.place(x=0, y=0)
    Label(user_page, text="Login or Register", font="LCDMono2 80 bold",
          background="blue").pack(pady=50)
    button = Button(user_page,
                    image=log,
                    command=login)
    button.pack()
    reg = PhotoImage(file="register.png")
    button = Button(user_page,
                    image=reg,
                    command=register)
    button.pack(pady=40)
    user_page.mainloop()
def first():
    global first_page
    first_page = Tk()
    first_page.title("QUIZ APPLICATION")
    first_page.geometry("1400x1000")
    first_page.config(background="white")
    bg = PhotoImage(file="first1.png")
    label1 = Label(first_page, image=bg)
    label1.place(x=0, y=0)
    logo = PhotoImage(file="ned logof.png")
    labelimage = Label(
        first_page,
        image=logo,
        background="white",)
    labelimage.pack(side="left", anchor="nw")
    labeltext = Label(
        first_page,
        text="Q U I Z",
        font=("Showcard Gothic", 60, "bold"),
        background="white",)
    labeltext.pack(pady=(0, 0), anchor="n", side="top")
    btnStart = Button(
        first_page,
        text="PLAY",
        font="LCDMono2 60 bold",
        borderwidth=10
        , relief=GROOVE,
        background="orange",
        command=user,)
    btnStart.pack(pady=200, padx=375)
    first_page.mainloop()
first()