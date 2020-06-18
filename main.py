def main():
    display_choice_menu()
    choice = input("Choose an option from above: ")
    while choice < 1 or choice > 4:
        print("Invalid choice")
        choice = input("Please choose a valid option: ")

def add_todo(todo_list, todo_item):
    todo_list.append(todo_item)

def display_choice_menu():
    print("1. View todo list")
    print("2. Add a new todo item")
    print("3. Remove an existing todo item")
    print("4. Exit program")

if __name__ == '__main__':
    main()