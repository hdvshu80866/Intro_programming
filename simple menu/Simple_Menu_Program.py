# Simple Menu Program
import example_function as function
# a stub for Main Menu Option 1: Display all Album
def load_albums():
    print("You select Play Existing Albums. Press enter to continue")
    value = input().strip()
    return value

# Option 2 should take you to another (sub) menu as follows:
def update_album_title():
    print("You selected Update Album Title. Press enter to continue")
    value = input().strip()
    return value

def update_album_genre():
    print("You selected Update Album Genre. Press enter to continue")
    value = input().strip()
    return value

def return_main_menu():
    value = input().strip()
    return value

def display_albums():
    while True:
        print("Display Albums Menu:")
        print("1 To Update Album Title")
        print('2 To Update Album Genre')
        print('3 To Enter Main Album')
        print('4 Exit')
        choice = function.read_integer_in_range("Please enter your choice:",1,4)
        if choice ==1:
            update_album_title()
        if choice ==2:
            update_album_genre()
        elif choice ==3:
            main_menu()
        elif choice ==4:
            break


def main_menu():
    while True:
        print("Main Menu:")
        print("1 Load Albums") #placeholder
        print("2 Display Albums")
        print("3 Exit")
        choice = function.read_integer_in_range("Please enter your choice:",1,3)
        if choice == 1:
            load_albums()
        if choice == 2:
            display_albums()
        elif choice == 3:
            break

if __name__ == "__main__":
    main_menu()