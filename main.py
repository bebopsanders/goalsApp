from makers.Usercreate import create_user
from makers.Taskcreate import create_task
from check.Accountchecker import check_account
print("Welcome to Goals!")
while True:
    acc_check = input("Already have account? y/n  ")
    if acc_check == "y":
        username = input("Enter your Username: ")
        check_account(username)
        see_list = input("View your Goal List? y/n  ")
        if see_list == "y":
            file_name = "goals/"+username+"'s goals.txt"
            with open(file_name, 'r') as file_object:
                for line in file_object:
                    print(line)
        create_task(username)
        break
    elif acc_check == "n":
        create_user()
        break
    else:
        print("Sorry I didn't understand {}".format(str(acc_check)))
