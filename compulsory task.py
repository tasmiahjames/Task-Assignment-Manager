#A program to help a small business assign and keep track of tasks

#Import modules
import os
from datetime import datetime

#Declare variables
first_login = True
current_path = os.path.dirname(__file__)

#Functions used within the program 
#Loops through user.txt and checks if the user inputs the username and corresponding password correctly and if not then the user can retry
def login():
    trueUser = False
    truePass = False

    # Loop until the user enters a username that is stored in user.txt
    while not trueUser:
        usern = input("What is your username?: ")
        for x in range(0, len(users)):
            if users[x][0] == usern:
                trueUser = True

                if trueUser:

                    #Loop until the user enters the correct password for the corresponding username
                    while not truePass:
                        password = input("What is your password?: ")
                        if users[x][1] == password:
                            truePass = True

                        if not truePass:
                            print("\nYour password is incorrect! Please retry.")
        if not trueUser:
            print("\nYour username is incorrect! Please try again")

        #Log in the user
        else:
            print("\nWelcome!")
            print("Enter \"-1\" at any time to return to the Main Menu")
    return usern

#If the admin inputs 'r' the user can add a new user to user.txt
def reg_user():
    usernameUnique = False
    passwordConfirm = False

    #Cross check that the username is "admin"
    if username == "admin":
        print("\nPlease enter the details of the new user below")

        #Make sure the admin is entering a new user and not a repeat
        while not usernameUnique:
            unique = True
            new_user = input("Provide a username please!:\t\t")

            #Return to main menu if the user ever enters "-1"
            if new_user == "-1":
                break
            
            #Make sure the user enters something, otherwise loop back and let
            elif new_user == "":
                print("\nPlease enter a valid username\n")
            
            #Cross check if the username already exists.
            else:
                for x in range(0, len(users)):
                    if users[x][0] == new_user:
                        print("\nThe username already exists! Please choose a different username.\n")
                        unique = False
                if unique:
                    usernameUnique = True

        if new_user == "-1":
            pass

        else:
            #Loop until the passwords match
            while not passwordConfirm:
                new_pass1 = input("Please provide a password:\t\t")
                if new_pass1 == "":
                    print("\nPlease enter a valid password.\n")
                elif new_pass1 == "-1":
                    break
                else:
                    new_pass2 = input("Confirm your password:\t")

                    if new_pass2 == "-1":
                        break

                    #If the usernames match print the new user details to screen and add the new user to user.txt
                    elif new_pass1 == new_pass2:
                        passwordConfirm = True
                        user.write(f"\n{new_user}, {new_pass1}")
                        print(f"\nA new user has been added!\nWith the username:\t{new_user}\n With the password:\t{new_pass1}")

                    else:
                        print("\nPasswords do not match :( Please retry.\n")

        #Write the username and password to user.txt
        passwordConfirm = False

    else:
        print("\nOnly the admin can register new users!")


#If the user inputs 'a' the user can add a new task to tasks.txt
def add_task():
    #Define variables
    info = []
    info_title = ["Username:\t", "Task Title:\t", "Description:\t", "Date Assigned:\t", "Due Date:\t", "Completed:\t"]
    skip = False

    #Loop through each task and save it in a list.
    for x in range(0, 6):
        while True:
            data = input(f"{info_title[x]}")
            
            #Make sure the user has entered valid data.
            if data == "":
                print("\nInvalid input :( Please try again.\n")
            else:
                info.append(data)
                break
        
        # If the user enters "-1" then return to main menu
        if info[x] == "-1":
            skip = True
            break

    #Check if the user wishes to return to the menu.
    if not skip:

        # Write the task to the file.
        task.write(f"\n{info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]}, {info[5]}")

        # Confirm the details by printing to the screen.
        print("\nA new task has been added")
        print("----------------------------------------------------")
        print("Username:\t" + info[0])
        print("Task Title:\t" + info[1])
        print("Description:\t" + info[2])
        print("Date Assigned:\t" + info[3])
        print("Due Date:\t" + info[4])
        print("Completed:\t" + info[5])
        print("----------------------------------------------------")


#If the user inputs 'va' the details of all tasks for all users are printed to the screen.
def view_all():
    print("\nView All Tasks")

    #Loop through each line of the 'tasks' list and print it.
    for line in tasks:
        print("----------------------------------------------------")
        print("Username:\t" + line[0])
        print("Task Title:\t" + line[1])
        print("Description:\t" + line[2])
        print("Date Assigned:\t" + line[3])
        print("Due Date:\t" + line[4])
        print("Completed:\t" + line[5])
        print("----------------------------------------------------")


# If the user inputs 'vm' all their personal tasks are printed for them.
def view_mine():
    user_found = False
    my_tasks = []
    print("\nView My Tasks")

    #Loop through all the tasks in the list.
    for x in range(0, len(tasks)):
        if username == tasks[x][0]:
            my_tasks.append(tasks[x])
            user_found = True

    #If the user is found, print each task assigned to the current user and add a task number to each task for easy access 
    if user_found:
        for x in range(0, len(my_tasks)):
            print(f"\nTask {x+1}")
            print("----------------------------------------------------")
            print("Username:\t" + my_tasks[x][0])
            print("Task Title:\t" + my_tasks[x][1])
            print("Description:\t" + my_tasks[x][2])
            print("Date Assigned:\t" + my_tasks[x][3])
            print("Due Date:\t" + my_tasks[x][4])
            print("Completed:\t" + my_tasks[x][5])
            print("----------------------------------------------------")

        #Request the user to input the task they wish to edit.
        while True:
            #Add a try / except block in case the user doesn't enter anything so it returns to menu
            try:
                task_num = int(input("Please enter a task number to edit: "))
                if task_num == -1:
                    break

                #Cross check the task number
                elif task_num > 0 and task_num <= len(my_tasks):
                    
                    #Remove, edit and re add the new task to tasks.txt
                    for x in range(0, len(my_tasks)):
                        tasks.remove(my_tasks[x])

                    #Loop until the user enters a valid option
                    while True:
                        print("\nPlease choose an option")
                        print("m - mark task as complete\ne - edit the task")
                        menu_choice = input()

                        #If the user chooses "m", edit the Completed to "Yes".
                        if menu_choice == "m":
                            my_tasks[task_num-1][5] = "Yes"
                            print(f"\nTask {task_num} has been marked as complete.")
                            break

                        elif menu_choice == "-1":
                            break

                        #If the user chooses "e", they can edit the Username and Due Date of the task.
                        elif menu_choice == "e":
                            if my_tasks[task_num-1][5] == "Yes":
                                print("\nThe task has been completed. Unable to edit.")
                                break
                            else:
                                print("\nPlease enter the new Username and Due Date")
                                usern = input("Edit Username:\t")
                                due_date = input("Edit Due Date:\t")
                                
                                #Check if the users inputs are not blank.
                                if usern != "":
                                    my_tasks[task_num-1][0] = usern
                                if due_date != "":
                                    my_tasks[task_num-1][4] = due_date

                                print("\nUpdated details")
                                print("Username:\t" + my_tasks[task_num-1][0])
                                print("Due Date:\t" + my_tasks[task_num-1][4])
                                break
                        
                        #Let the user know if the input is not recognised
                        else:
                            print("\nUnrecognized input.")

                    #Add the newly edited tasks in "my_tasks" to "tasks".
                    task.seek(0)
                    task.truncate(0)
                    for x in range(0, len(my_tasks)):
                        tasks.append(my_tasks[x])
                    for x in range(0, len(tasks)):
                        task.write(", ".join(tasks[x]))
                        if x != len(tasks)-1:
                            task.write("\n")
                    break
                
                #Let the user know if the task entered does not exist.
                else:
                    print("\nThe selected task does not exist. Please try again.\n")
            except:
                print("\nNo task number entered. Please try again.\n")
                

    #Let the user know if they have no tasks.
    if not user_found:
        print("No tasks found for selected user.")


#If the user inputs 'ds' statistics are shown
def display_statistics():
    
    #Check if the user is "admin"
    if username == "admin":
        
        #Generate reports constantly
        generate_reports()

        #open files
        task_over_r = open(os.path.join(current_path, "task_overview.txt"), "r+")
        user_over_r = open(os.path.join(current_path, "user_overview.txt"), "r+")

        #Adjust format
        for line in task_over_r:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

        for line in user_over_r:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))
            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

    #If the user is not "admin" let them know they are not authorised to use this function.
    else:
        print("\nYou are not authorised to view statistics.\n")

#If the user inputs 'gr' reports are generated with statistics about the tasks and each user.
def generate_reports():

    #Check if the logged in user is "admin"
    if username == "admin":

        #Open the files and set them to write
        task_over_w = open(os.path.join(current_path, "task_overview.txt"), "w+")
        user_over_w = open(os.path.join(current_path, "user_overview.txt"), "w+")
        
        #Define variables
        total_tasks = len(tasks)
        num_completed = 0
        num_incomplete = 0
        num_inc_overdue = 0
        per_incomplete = 0
        per_overdue = 0

        #Loop through each task and update the variables based on the information for each task.
        for x in range(0, len(tasks)):
            if tasks[x][5] == "Yes":
                num_completed += 1
            elif tasks[x][5] == "No":
                num_incomplete += 1

                #Convert the Due Date to a datetime object and compare the current date to the due date.
                task_date = datetime.strptime(tasks[x][4], '%d %b %Y')
                if datetime.date(datetime.now()) < task_date.date():
                    num_inc_overdue += 1

        if total_tasks == 0:
            per_incomplete = 0
            per_overdue = 0
        else:
            per_incomplete = round(100*num_incomplete/total_tasks)
            per_overdue = round(100*num_inc_overdue/total_tasks)

        #Write the statistics to the file.
        task_over_w.write("~ Task Overview ~\n\n")
        task_over_w.write(f"Total Tasks:\t\t{total_tasks}\nCompleted Tasks:\t{num_completed}\nIncomplete Tasks:\t{num_incomplete}\nOverdue Tasks:\t\t{num_inc_overdue}\nPortion Incomplete:\t{per_incomplete}%\nPortion Overdue:\t{per_overdue}%")

        #Write the initial statistics to the file.
        num_users = len(users)
        user_over_w.write("~ User Overview ~\n\n")
        user_over_w.write(f"Total Users:\t\t{num_users}\n")
        user_over_w.write(f"Total Tasks:\t\t{total_tasks}")

        #Reset the variables for each user
        for x in range(0, len(users)):
            num_tasks = 0
            num_completed = 0
            num_incomplete = 0
            num_inc_overdue = 0
            per_incomplete = 0
            per_overdue = 0
            per_completed = 0
            por_tasks = 0

            user_over_w.write("\n----------------------------------------------------\n")
            user_over_w.write(f"User:\t\t\t\t\t{users[x][0]}\n")

            #Loop through each task
            for y in range(0, len(tasks)):

                #Check if the task is assigned to the current user
                if users[x][0] == tasks[y][0]:
                    num_tasks +=1
                    if tasks[y][5] == "Yes":
                        num_completed += 1
                    elif tasks[y][5] == "No":
                        num_incomplete += 1
                        task_date = datetime.strptime(tasks[y][4], '%d %b %Y')
                        if datetime.date(datetime.now()) < task_date.date():
                            num_inc_overdue += 1

            if num_tasks == 0:
                per_incomplete = 0
                per_overdue = 0
                per_completed = 0
            else:
                per_incomplete = round(100*num_incomplete/num_tasks)
                per_overdue = round(100*num_inc_overdue/num_tasks)
                per_completed = round(100*num_completed/num_tasks)

            if total_tasks == 0:
                por_tasks = 0
            else:
                por_tasks = round(100*num_tasks/total_tasks)

            #Write the statistics to the file again
            user_over_w.write(f"User Tasks:\t\t\t\t{num_tasks}\nPortion Total Tasks:\t{por_tasks}%\nPortion Completed:\t\t{per_completed}%\nPortion Incomplete:\t\t{per_incomplete}%\nPortion Overdue:\t\t{per_overdue}%")
            user_over_w.write("\n----------------------------------------------------\n")
        
        #Close the files
        print("\nReports have been generated: task_overview.txt, user_overview.txt")
        task_over_w.close()
        user_over_w.close()
    else:
        print("\nYou are not authorised to generate reports.\n")


#Loop that will run until the user exits
while True:

    #Open the text files and read the contents into a list variable.
    user = open(os.path.join(current_path, "user.txt"), "r+")
    users = user.readlines()
    users = [x.strip().split(", ") for x in users]

    task = open(os.path.join(current_path, "tasks.txt"), "r+")
    tasks = task.readlines()
    tasks = [x.strip().split(", ") for x in tasks]

    #Check if the user has logged in yet
    if first_login:
        username = login()
        first_login = False    
    
    #Print the menu
    if username == "admin":
        print("\nPlease select one of the following options:")
        print("r - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit")
        menu = input("")
    else:
        print("\nPlease select one of the following options:")
        print("a - add task\nva - view all tasks\nvm - view my tasks\ne - exit")
        menu = input("")

    #run the funtions based on user input
    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds":
        display_statistics()

    elif menu == "gr":
        generate_reports()

    #If the user inputs 'e' the main loop is stopped and the program exits.
    elif menu == "e":
        break

    #If the input the user has entered is not recognised the user is notified and the loop starts again.
    else:
        print("\nInvalid input. Please retry.")

    #close files
    user.close()
    task.close()