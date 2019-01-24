# 1. provide a menu to the user


def show_menu():
    print("Here is what you can do with this program")
    print("Press 1. To Add a new date of birth")
    print("Press 2. To update a date of birth")
    print("Press 3. To delete a date of birth")
    print("Press 4. To lookup a date of birth")
    print("press 5. To Quit")
    choice = int(input("Please enter your choice"))
    if choice < 1 or choice > 5:
        print("please enter a valid choice")
        show_menu()
    else:
        return choice


def add_newdob(date_of_birth_dict):
    name = input("please enter a name")
    dob = input("please enter date of birth")
    if name in date_of_birth_dict:
        print("the entered name already exists")
    else:
        date_of_birth_dict[name] = dob
    pass


def update_dob(date_of_birth_dict):
    name = input("please enter the name for update")
    if name in date_of_birth_dict:
        dob = input("please enter date of birth")
        date_of_birth_dict[name] = dob
    else:
        print("the entered name doesnt exist")
    pass


def delete_dob(date_of_birth_dict):
    name = input("please enter a name for delete")
    if name in date_of_birth_dict:
        del date_of_birth_dict[name]
    else:
        print("the entered name doesnt exist")
    pass


def lookup_dob(date_of_birth_dict):
    #
    pass


def main():
    choice = show_menu()
    date_of_birth_dict = {}
    while choice != 5:
        if choice == 1:
            add_newdob(date_of_birth_dict)
        elif choice == 2:
            update_dob(date_of_birth_dict)
        elif choice == 3:
            delete_dob(date_of_birth_dict)
        else :
            lookup_dob(date_of_birth_dict)
        choice = show_menu()
    else:
        print(date_of_birth_dict)
        print("Program completed execution")

main()