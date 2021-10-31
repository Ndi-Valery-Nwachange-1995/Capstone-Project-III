import datetime  # import datetime

# python program that help to manage task assigned to each member of the team in a small business.

# defining the user dictionary
users = {}

# open and reading from users.txt as username
with open('user.txt', 'r') as username:
    # line in username
    for line in username:
        # username , password is initialize to line.split(", ") which is putting new line character in all the comma
        # and space (,) in username and password.
        username, password = line.split(",")

        # strip removes leading/trailing whitespaces
        users[username.strip()] = password.strip()

# getting the username from the user through the keyboard
name = input("Enter your username:\n")

# while name not in users
while not name in users:
    # display username incorrect.
    print("Username incorrect.")

    # getting the username valid from the user through the keyboard
    name = input("Enter a valid username:\n")

# if name in users:
if name in users:
    # display username correct.
    print("Username correct")

# open and reading from users.txt as password
with open('user.txt', 'r') as password:
    # for line in password:
    for line in password:
        # username , password is initialize to line.split(", ") which is putting new line character in all the comma
        # and space (,) in username and password
        username, password = line.split(",")

        # strip removes leading/trailing whitespaces
        users[password.strip()] = username.strip()

# getting the password from the user through the keyboard
password = input("Enter your password:\n")

# while password not in users:
while not password in users[name]:

    # display your username is correct but your password is incorrect.
    print("Your username is correct but your password is incorrect.")

    # getting the valid password from the user through the keyboard
    password = input("Enter a valid password:\n")

# initializing menu to None
menu = None

# if name is equal to 'admin':
if name == 'admin':

    # menu is initialize to all the string in task task.txt
    menu = (input(
        "\nSelect one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - "
        "view my tasks\ns - statistics\ne - exit\n"))

# elif menu is not equal to 'admin':
elif menu != 'admin':

    # menu is initialize to all the string in task task.txt
    menu = (input(
        "\nSelect one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - "
        "view my tasks\ne - exit\n"))

# if menu is equal to read with lowercase(r) or menu is equal to read with uppercase(R) and name is equal to 'admin':
if (menu == "r" or menu == "R") and name == 'admin':

    # new_user is initialize to new user name entered by the user through the keyboard
    new_user = (input("Enter a new user name:\n"))

    # while new_user in user
    while new_user in users:
        # display user already exist
        print("user already exists")

        # enter a user that does not exist
        new_user = input("enter a user that does not exist: \n")

    # new_password is initialize to new password entered by the user through the keyboard
    new_password = (input("Enter a new password: \n"))

    # asking user to input same password for confirmation
    new_password_confirm = input("confirm the password: \n")

    # while new_password is not equal to new_password_confirm
    while new_password != new_password_confirm:
        # entering same password with use of keyboard to confirm password
        new_password_confirm = input("confirm your password: \n")

    # open 'user.txt' append('a') as username
    with open('user.txt', 'a') as username:

        # username.write new line plus(+) new_user plus(+) comma and space(", ") plus(+) new_password.
        username.write("\n" + new_user + ", " + new_password)

# elif menu is equal to append("a") with lowercase or menu is equal to append("A") with uppercase
elif menu == "a" or menu == "A":

    # task is initialize to the username of the person the task is assigned to entered by the user and saved to
    # 'task.txt
    user_task = input("Enter the username of the person the task is assigned to.\n")

    # task_title is initialize to the title of the task entered by the user and saved to 'task.txt
    task_title = input("Enter the title of the task.\n")

    # task_description is initialize to the task description entered by the user and saved to 'task.txt
    task_description = input("Enter the task description.\n")

    # task_due is initialize to the due date of the task. (yyyy-mm-dd) entered by the user and saved to 'task.txt'
    task_due = input("input the due date of the task. (yyyy-mm-dd)\n")

    # date is initialize to datetime.date.today()
    date = datetime.date.today()

    # task_complete is initialize to 'No'
    task_completed = 'No'

    # open 'tasks.txt append('a') as task:
    with open('tasks.txt', 'a') as tasks:

        # task.write new line plus(+) name plus(+) comma and empty space(", ") plus(+) task_description plus(+) comma
        # and empty space(", ") plus(+) str(date) plus(+) comma and empty space(", ") plus(+) task_due plus(+) comma
        # and empty space(", ") plus(+) task_completed.
        tasks.write("\n" + user_task + ", " + task_title + ", " + task_description + ", " + str(
            date) + ", " + task_due + ", " + task_completed)

# elif menu is equal to "va" with lowercase or menu is equal to "VA" with uppercase and name is equal to 'admin'
elif menu == "va" or menu == "VA":

    # all_task is open 'tasks.txt read('r')
    all_tasks = open('tasks.txt', 'r')

    # for line in all_tasks
    for line in all_tasks:
        # task_list is initialize to line.split(", ") that is putting comma and space in task_list
        task_list = line.split(", ")

        # display task plus(+) task_list at index [1]
        print("Task:\t " + task_list[1])

        # display assigned to plus(+) task_list at index [0]
        print("Assigned to:\t" + task_list[0])

        # display Date assigned plus(+) task_list at index [3]
        print("Date assigned:\t" + task_list[3])

        # display Due date plus(+) task_list at index [4]
        print("Due date:\t" + task_list[4])

        # display task complete plus(+) task_list at index [5]
        print("Task Complete:\t" + task_list[5].strip('\n'))

        # display Task description plus(+) task_list at index [2]
        print("Task description:\n" + task_list[2])

        # print new line
        print("\n")

    # close all_tasks in the for loop
    all_tasks.close()

# menu is equal to "vm" with lowercase or menu is equal to "VM" with uppercase
elif menu == "vm" or menu == "VM":

    # filename is initialize to open ('tasks.txt , 'r') that is reading filename in tasks.txt
    filename = open('tasks.txt', 'r')

    # for line in filename:
    for line in filename:

        # task_list is initialize to line.split(', ") that is putting comma and space in task_list
        task_list = line.split(", ")

        # if name is equal to task_list[0] that index [0]
        if name == task_list[0]:
            # display Task plus(=) task_list at index [0]
            print("Task:\t" + task_list[0])

            # display Assigned to plus(+) task_list at index [1]
            print("Assigned to:\t" + task_list[1])

            # display Date assigned plus(+) task_list at index [3]
            print("Date assigned:\t" + task_list[3])

            # display Due date plus(+) at index [4]
            print("Due date:\t" + task_list[4])

            # display Task complete plus(+) task_list at index [5]
            print("Task complete:\t" + task_list[5].strip('\n'))

            # display Task description plus(+) task_list at index [2]
            print("Task description:\n" + task_list[2])

            # print new line
            print("\n")

    # close filename in for loop
    filename.close()

# initializing task_num to zero(0)
tasks_num = 0

# initializing users_num to zero(0)
users_num = 0

# if menu is equal to 's':
if menu == 's':

    # open and read tasks.txt as all_tasks
    with open("tasks.txt", "r") as all_tasks:

        # for line in all_tasks:
        for line in all_tasks:

            # initializing tasks_num to plus(+) equal 1
            tasks_num += 1

        # displaying the content of tasks_num
        print(f"\nThe total number of tasks is: {tasks_num}")

    # open user.txt and read as username:
    with open("user.txt", "r") as username:

        # for line in username:
        for line in username:

            # initializing users_num to plus(+) equal to 1
            users_num += 1

        # displaying the content of users_num
        print(f"The total number of users is: {users_num}")
