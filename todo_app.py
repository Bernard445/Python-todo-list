tasks = []

def main_menu ():
    print('Welcome')
    print('1. Add Task')
    print('2. View Task')
    print('3. Delete Task')
    print('4. Quit')

    choice = input('Enter your choice  1, 2, 3, 4 ')
    return choice

    try:
        if choice not in ["1", "2", "3", "4"]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")



def add_task():
    new_task = input("Please enter your task: ")
    if new_task.strip() == "":
        print("Task cannot be empty.")
        return
    tasks.append(new_task)
    print("Task added!")


def view_task():
    if not tasks:
        print("There are no tasks to view.")
        return

    print("Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task():
    if not tasks:
        print("There are no tasks to delete.")
        return

    print("Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    try:
        delete_num = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        if delete_num < 1 or delete_num > len(tasks):
            print("Task number out of range.")
        else:
            deleted = tasks.pop(delete_num - 1)
            print(f"Task '{deleted}' deleted.")
    finally:
        print("Returning to main menu...")


    



while True:
    choice = main_menu()

    # input validation using error handling
    try:
        if choice not in ["1", "2", "3", "4"]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break







