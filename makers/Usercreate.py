def create_user():
    while True:
        user_name = input("Enter a cool username: ")
        password = input("Enter a gnarly password: ")
        nickname = input("What should we call you: ")
        file_name = "users/"+user_name+".txt"
        goal_file_name = "goals/"+user_name+"'s goals.txt"
        with open(file_name, 'w') as file_object:
            file_object.write("{},{},{}".format(nickname,password,user_name))
        with open(goal_file_name, 'w') as file_object:
            file_object.write(str(user_name+" Goal List:\n"))
        break
