from datetime import datetime

print("Welcome to Quelibb Diary")
users_access_details = []
users_activity_details = {}


def confirm_del(value, username):
    to_be_deleted = int(input("\nTitle number: "))
    print("\n" * 15)
    print("To delete, press enter")
    print(value[to_be_deleted - 1])
    confirmation = input("To delete, press enter")
    if confirmation == "":
        del value[to_be_deleted - 1]
        print("\n" * 15)
        cont = input("Successfully deleted\nPress enter to continue\n")
        if cont == "":
            print("\n" * 15)
            main_menu(username)
    else:
        print("\n" * 15)
        delete(username)


def delete(username):
    if any(users_activity_details):
        for key, value in users_activity_details.items():
            if key == username:
                count = 1
                if isinstance(value, list):
                    print("Select entry you would like to delete\nTitles:")
                    for val in value:
                        print(count, val["title"])
                        count += 1
                    confirm_del(value, username)

                elif isinstance(value, dict):
                    print("Select entry you would like to delete\nTitles:")
                    print(count, value["title"])
                    print("\n" * 15)
                    print("To delete, press enter")
                    print(value)
                    confirmation = input("To delete, press enter")
                    if confirmation == "":
                        del value
                        print("\n" * 15)
                        cont = input("Successfully deleted\nPress enter to continue\n")
                        if cont == "":
                            print("\n" * 15)
                            main_menu(username)
                    else:
                        print("\n" * 15)
                        delete(username)

    else:
        print("Emtpy storage, make an entry!")
        main_menu(username)


def save_entries(temp_db):
    for key, value in temp_db.items():
        if key in users_activity_details:
            if isinstance(users_activity_details[key], list):
                users_activity_details[key].append(value)
            else:
                temporary_list = [users_activity_details[key]]
                temporary_list.append(value)
                users_activity_details[key] = temporary_list
        else:
            users_activity_details[key] = value


def create_entries(username):
    diary_db = {username: {}}
    today = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    print("It's " + today)
    title = str(input("\nTitle: "))
    body = str(input("Dear Diary, \n"))
    diary_db[username] = {"date": today, "title": title, "body": body}
    save_entries(diary_db)
    print("\n" * 15)


def login():
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    if any((users["username"] == username for users in users_access_details)):
        if any(users["password"] == password for users in users_access_details):
            print("\n" * 15)
            print("Login successful!")
            print("Hello " + username + ", Welcome back!")

            main_menu(username)
        else:
            print("\n" * 15)
            print("Invalid password")
            login()
    else:
        print("\n" * 15)
        print("Username does not exist")
        welcome()


def signup():
    username = input("Go ahead, name your diary: ")
    if any(users["username"] == username for users in users_access_details):
        print("\n" * 15)
        print("Oops, username already exists")
        signup()
    password = str(input("Input a 4-digit password to safelock diary: "))
    while len(password) != 4:
        print("\n" * 15)
        password = str(input("Invalid password length\nInput a 4-digit password to safelock diary: "))
    new_user = {"username": username, "password": password}
    users_access_details.append(new_user)
    print("\n" * 15)
    print("\nWelcome " + username.title() + ",\nYour diary has been created!")
    login_password = str(input("Input password to login: "))
    while login_password != new_user["password"]:
        print("\n" * 15)
        login_password = str(input("Incorrect password\nInput correct password to login: "))
    print("\n" * 15)

    main_menu(username)


def welcome():
    option = int(input("""
Main Menu:
  1. Login
  2. New account, Sign up
  3. Quit Quelibb\n"""))

    print("\n" * 15)
    if option == 1:
        return login()
    if option == 2:
        return signup()
    if option == 3:
        print("Thank you")


def menu(option, username=""):
    if option == 2:
        create_entries(username)


def main_menu(username):
    option = int(input("""
What would you like to do today?
  1. Find entry
  2. Create new entry
  3. Delete unwanted entry
  4. View all entries in my diary

To logout, press 0\n"""))
    print("\n" * 15)

    if option == 2:
        menu(option, username=username)
        main_menu(username)
    elif option == 0:
        print("\n" * 15)
        welcome()
    elif option == 4:
        for key, details in users_activity_details.items():
            if key == username:
                count = 1
                print(key.title() + "'s Entries:")
                if isinstance(details, list):
                    for each_detail in details:
                        print(count, each_detail)
                        count += 1
                elif isinstance(details, dict):
                    print(count, details)
                    print()
        cont = input("To return back to menu, press enter")
        if cont == "":
            main_menu(username)
    elif option == 3:
        delete(username)
    elif option == 1:
        if any(users_activity_details):
            for key, value in users_activity_details.items():
                if key == username:
                    count = 1
                    if isinstance(value, list):
                        print("Input title number you would like to view\nTitles:")
                        for val in value:
                            print(count, val["title"])
                            count += 1
                        to_be_viewed = int(input("\nTitle number: "))
                        print("\n" * 15)
                        print(value[to_be_viewed - 1])
                        cont = input("To continue, press enter")
                        if cont == "":
                            print("\n" * 15)
                            main_menu(username)
                    elif isinstance(value, dict):
                        print("Select entry you would like to view\nTitles:")
                        print(count, value["title"])
                        print("\n" * 15)
                        print(value)
                        cont = input("To continue, press enter")
                        if cont == "":
                            print("\n" * 15)
                            main_menu(username)
        else:
            print("No entry found!")
            main_menu(username)
    else:
        print("Invalid option")
        main_menu(username)

 
welcome()
# print(users_access_details)
# print(users_activity_details)
# # print(all_entries)
