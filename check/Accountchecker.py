def check_account(username):
    elems = []
    with open("users/"+username+".txt",'r') as file_object:
        for i in file_object:
            split_line = i.split(",")
            elems.append(split_line)
    print("Found you {}!".format(str(elems[0][0])))
    pass_check = True
    while pass_check:
        password = input("Confirm your password: ")
        if password == elems[0][1]:
            pass_check = False
        else:
            print("Bad password, please try again!\n")
            continue
