import random
logged_in = False # The logged_in variable is initialized as False at the beginning of the program.

def login(name, password):    # To take the name and password of the user to login
        """
        Name: login\n
        Return value: None\n
        Parameters: (name -> str, password -> str), a username and password (string type.)\n
        Description: 
                Takes the username and password that has been inputted by the user and verifies it through the user_details file.
        """

        global granted,user_name
        granted = False
        user_name = name
        with open("user_details.txt", "r", encoding="utf8") as file: #If name and password are available in the user_details file, the user will be authenticated and the program will continue.
            if name+","+password+"\n" in file.readlines():
                print("\n\t\t\t*** Login Successful ***\t\t\t")
                granted = True
                quiz()
            else:
                print("\n\t\t**** Wrong user name or password ****\t\t")
                granted = False
                begin()
def register(name, password):  # To take the name and password of the user to register
        
        """
        Name: register\n
        Return value: None\n
        Parameters: (name -> str, password -> str), a username and password (string type.)\n
        Description:
                This function registers the user to the portal, and is saved in the user_details file, so it can operate on the next program execution.
        """
        
        global granted
        with open("user_details.txt", "a", encoding="utf8") as file:
            if check(name)=="Valid": # Calls the check function (below) and uses the return value to confirm whether the username already exists. 
                file.write(name + "," + password + "\n")
                print("\n\t*** You Are Successfully Registered! ***\t\n")
            else:
                print("\n\t\t***  You are Already Registered!  ***\t\t")
        granted = False # After registration, the begin function is called, prompting the user to login or register.
        begin()
def access(option): # A function that asks the user for input and produces the desired output.
        
        """
        Name: access\n
        Return value: None\n
        Parameters: (option -> str), (string type)\n
        Description: 
                Receives a string value containing "login" or "reg" (register) and gives a result depending on the input.
        """
        
        if option == "login":
            login(input("\nEnter Your Username\n→ "), input("Enter Your Password\n→ "))
        else: # In the case a user inputs registration, the 'register' function is called (above) with two parameters, username and password.
            print("\n\t***Enter your name and password to register to our Portal***\t\n")
            register(input("\nEnter Your Username\n→ "), input("Enter Your Password\n→ ")) # Calls register function with username and password parameter.
def begin():
        
        """
        Name: begin\n
        Return value: None\n
        Parameters: () -> None\n
        Description:
                Asks the user for input and calls the access function if it is a valid entry.
        """
        
        option = input("\nLogin or Register (login,reg): ").lower()
        if option != "login" and option != "reg":
            begin()
        else:
            access(option)
def check(name): # Runs a code responsible for checking if the user is already registered.
    
    """
    Name: check\n
    Return value: ['Exists' or 'Valid'], if the username is already in the file, the function will return 'Exists' else it will return 'Valid'\n
    Parameters: (name -> str), (string type.)\n
    Description:
            This function checks the user_details file to confirm that the username does not exist.
    """
    
    with open("user_details.txt","r") as f: # The code reads all the lines in a file.
        for user in f.readlines(): # and then splits each line by the comma, the first entry is the username.
            if name in user.split(",")[0]:
                return "Exists" # checks whether it matches with inputted username.
        return "Valid" # returns Valid if the name doesn't exist in the file.
def first_page(): # The first function.
    
    """
    Name: first_page\n
    Return value: None\n
    Parameters: () -> None\n
    Description:
            This is the first globally called function in the program, The user enters the appropriate input and its progresses further.
    """
    
    global logged_in, option, usernam, pwd
    if not logged_in: #if variable logged_in is false [is False at beginning], then it asks whether you login as admin or a user.
        print("\n\t\t===============================\n\t\tWelcome to our Quiz Application\n\t\t===============================")
        option = input("\n\t\t  ARE YOU USER OR ADMIN \n\n\t\t\tADMIN(a)\n\t\t\tUSER(u)\n\n\t\t  PRESS 'q' TO QUIT\n→ ").lower()
    if option == "a":
        if not logged_in: # Logs in as admin, and sets logged_in to True to skip login form after doing an action.
            print("\nFor ADMIN controls enter username and password!")
            usernam = input("ENTER USERNAME\n→ ")
            pwd = input("ENTER PASSWORD\n→ ")
        if usernam == "admin" and pwd == "123": # After logging in, the variables usernam,pwd are set and will apply on the next call of the function, ---
            if not logged_in:
                print("\nLogged in as ADMIN")
            logged_in = True # --- skipping above code on next call, unless logged_in is set to False.
            choice_admin = input("\nVIEW QUESTIONS(v), ADD QUESTIONS(a), DELETE QUESTIONS(d), CHECK SCORES(s), LOGOUT (l)\n→ ").lower()
            if choice_admin == "v":
                area_level = input("Please select the knowledge area of the questions you would like to see.\nSCIENCE EASY (SE)\nSCIENCE MEDIUM (SM)\nSCIENCE HARD (SH)\nGENERAL KNOWLEDGE EASY (GE)\nGENERAL KNOWLEDGE MEDIUM (GM)\nGENERAL KNOWLEDGE HARD (GH)\n→ ").lower()
                try: # In case the user doesn't input a valid entry, an error is raised and the error message is read.
                    with open ('{}.txt'.format(area_level),'r',encoding='utf8') as f:
                            contents=f.readlines()
                            for index in range (len(contents)):
                                    QAns=contents[index].split('|')
                                    print('Q{}:'.format(index+1)+QAns[0].replace('\\n','\n')+'\n'+"→ Ans:"+QAns[1].replace('\\n','\n')+"\n")#prints questions with the correct answer
                except:
                        print("\n\t\t\t*** INVALID ENTRY ***\t\t\t")
            elif choice_admin == "a":
                while True:
                    print("Please the select knowledge area where you would like to add further questions.")
                    area_level = input("\nSCIENCE EASY(SE)\nSCIENCE MEDIUM (SM)\nSCIENCE HARD (SH)\nGENERAL KNOWLEDGE EASY (GE)\nGENERAL KNOWLEDGE MEDIUM (GM)\nGENERAL KNOWLEDGE HARD (GH)\n→ ").lower()
                    try: # If user inputs incorrect entry, an error is raised.
                        with open('{}.txt'.format(area_level),"a",encoding="utf8") as q: 
                            q.write("{}\\n(a){}\\n(b){}\\n(c){}|{}|".format(input("Enter Question:"),input("Enter Option (a):"),input("Enter Option (b):"),input("Enter Option (c):"),input("Enter Ans:")).replace(",","\\n")+"\n") #the commas are replaced by '\\n' (so that the contents remain on one file, to avoid a new line during appending.), after it is written, a new line is added to make way for the next question.
                            print("YOUR QUESTION HAS BEEN ADDED TO QUESTION LIST ")
                            break
                    except:
                            print("\n\t\t\t*** INVALID ENTRY ***\t\t\t")
                            continue
            elif choice_admin == "s":
                    with open("results.txt") as f:
                        print("\nTHESE ARE THE RESULTS\n"+f.read())
            elif choice_admin == "l": # The variable logged_in is set to false, and it prompts the user for credentials on the next function call.
                print("\n\t\t*** You have Successfully logged out ***\t\t")
                logged_in = False
            elif choice_admin == "d":
               while True:
                    print("Please the select knowledge area where you would like to add further questions.")
                    area_level = input("\nSCIENCE EASY(SE)\nSCIENCE MEDIUM (SM)\nSCIENCE HARD (SH)\nGENERAL KNOWLEDGE EASY (GE)\nGENERAL KNOWLEDGE MEDIUM (GM)\nGENERAL KNOWLEDGE HARD (GH)\n→ ").lower()
                    try:
                        with open(f"{area_level}.txt","r",encoding="utf8") as q:
                            delete = q.readlines()
                            for no,i in enumerate(delete): QAns = i.split("|"); print("\nQ{}: ".format(no+1)+QAns[0].replace("\\n","\n")+"\n→ Ans:"+QAns[1])
                            print("\nEnter question number of what you want to delete.")
                            delete.pop(int(input(">>> "))-1)
                        with open(f"{area_level}.txt","w",encoding="utf8") as file: 
                            for i in delete: file.write(i)
                            break
                    except:
                            print("\n\t\t\t*** INVALID ENTRY ***\t\t\t")
                            continue
            first_page()

        else:
            print("**INCORRECT CREDENTIALS**")
            first_page()
    elif option == "u":
        begin()
    elif option == "q":
        print("\n\t\t***THANKS FOR VISITING***")
        quit()
    else:
        print("INCORRECT")
        first_page()

def test(file):

        """
        Name: test\n
        Return value: list[str], it returns the quiz file, so that it may be used to check answers further into the program.\n
        Parameters: (file -> str),(string type)\n
        Description:
                This function is responsible for the execution of the quiz game.
        """

        global score # Takes score as global, to pass the variable to another function so that it can calculate marks obtained.
        with open(file,"r",encoding="utf8") as q: # The file passed as a parameter will open the quiz file.
            quiz = q.readlines()
            index=0
            score=[]
            result=0
            random.shuffle(quiz) # All the variables will be initialized and the quiz will be shuffled.
            while index!=10: # ^ The readlines method reads the entire file and turns every line into an element of a list. (A while loop is used for the previous question feature, otherwise a for loop would be used.)
                answer = quiz[index].replace("\\n","\n")
                answer=answer.split("|")[1] # Take index as '0', the first element in 'quiz' (explained above) which is a string, "\\n" (explained in Admin Add Questions.) is replaced with "\n" to push options into the next line, then it is splitted, seperating the answer '[1]'
                print("\nQ{}: ".format(index+1)+quiz[index].replace("\\n","\n").split("|")[0]) # The same as above, except '[0]' is taken except of '[1]', 0 is the question and 1 is the answer, which is splitted by "|", explained above.
                if index!=0:
                        input_answer = input("\n(* FOR PREVIOUS) ENTER ANSWER: ") # ]
                elif index==0:
                        input_answer = input("\nENTER ANSWER: ")                # ] Removes the previous question indicator if the user is at the first question.
                if input_answer==answer:
                        score.append(1)
                        index+=1 # If the answer is valid, a point is added into the score list.
                elif input_answer=="*" and index!=0:
                        index-=1
                        score.pop(-1) # If the user wants to go back, they input the '*' sign and the index is subtracted by 1, also removing the last point of the user.
                elif input_answer=="*" and index==0:
                        print("CAN'T GO BEFORE FIRST QUESTION.") # The program will respond that the user can't previous before the first question.
                elif input_answer.lower() not in ["a","b","c","*"]:
                        print("\n\t***ENTER A,B or C***") # If the user doesn't enter from one of the options, the program will point it out.
                else:
                        index+=1
                        score.append(0) # If the user gets the wrong answer, '0' will be added to the score list.
        for point in score:
                result = result+point # All the points in the list are added into an int.
        score = result
        return quiz # The function returns the quiz file, so that the user may check their answers.
def checkanswers(quiz):
        
        """
        Name: checkanswers\n
        Return value: None\n
        Parameters: (quiz -> list[str]), (a list containing strings.)\n
        Description:
                This function checks the answers of the quiz after completion, if the user has given permission.
        """
        
        for number,question in enumerate(quiz):
            print("\nQ{}: ".format(number+1)+question.replace("\\n","\n").split("|")[0])
            print("ANSWER: "+question.replace("\\n","\n").split("|")[1])
            if number==9: break
def run(knowledge_area):
        
        """
        Name: run\n
        Return value: None\n
        Parameters: (knowledge_area -> str), (string type)\n
        Description:
                This function prompts the user for their difficuly level and assigns the appropriate quuestions for the quiz.
        """
        
        while True:
            level = input("\nWhich difficulty level you want to attempt:\nEasy (E)\nMedium (M)\nHard (H)\n→ ").lower() #Asks for difficulty level.
            if level in ["e", "m", "h"]: break # If the input is from one of these, the code will progress further.
        input("\n\t\t\t*** PRESS ENTER TO START ***\t\t\t")
        if knowledge_area == "s": quiz_file = test("s{}.txt".format(level)) # From the above input, the quiz with the difficulty level and knowledge area will begin.
        elif knowledge_area == "g": quiz_file = test("g{}.txt".format(level)) # A variable quiz is made with the return value of the function, which is the quiz file. used for checking answers.
        print(f"\nSCORE IS →  {score}",f"\nPERCENTAGE IS → {(score / 10) * 100} %")# Percentage is calculated ( (Obtained Marks/Total Marks) * 100)
        if input("\n\t\t Do you want to save this score?(Y) \t\t\n→ ").lower() == "y": # Asks to save, if 'y' then saves in results.txt file.
            with open("results.txt", "a+", encoding="utf8") as sr:
                sr.write(user_name.upper() + " --> " + str(score) + "\n")
                print("\n\t\t*** Your Score Has Been SAVED in Results ***\t\t")
        check_ans = input("\n\t\t Do you want to check answers?(Y)\t\t\n→ ").lower() # Asks to check answers, on yes, the function checkanswers will be called with the quiz file as a parameter.
        if check_ans == "y": checkanswers(quiz_file)
        if input("\n\t\t Do you want to play again?(Y)\t\t\n→ ").lower() == "y":
            quiz() # Which run the quiz function again if the user want to play again.
        else:
            print(f"\n\t\t*** THANKS FOR PLAYING {user_name.upper()} ***\t\t\n\n\t\t*** LOGGED OUT ***\n\n")
            granted = False
            first_page() # If the user doesn't want to play again, it will thank you for playing and then the program will be terminated.
def quiz():
        
    """
        Name: quiz\n
        Return value: None\n
        Parameters: () -> None\n
        Description:
                This function prompts the user for their knowledge area, and the run function is called with their input as the parameter.
    """
    while True:
            knowledge_area = input("\nSELECT A KNOWLEDGE AREA\nGeneral Knowledge(G)\nScience(S)\n→ ").lower()
            if knowledge_area == 's' or knowledge_area == 'g':
                    run(knowledge_area)
                    break
    if granted: #If granted is true, the quiz progam will begin, after it has finished execution, the user will be asked if they want to play again.
        quiz()
    elif not granted:
        begin() #If the user is not authenticated, the begin function will be called again, which will call the begin function, repeating until the user is authorized.
first_page() #Begins the program.