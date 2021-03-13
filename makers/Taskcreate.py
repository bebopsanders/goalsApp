def create_task(username):
    file_name = "goals/"+username+"'s goals.txt"
    while True:
        goal_name = input("Enter a goal you're going to complete: ")
        with open(file_name, 'a') as file_object:
            file_object.write(goal_name + "\n")
            break
