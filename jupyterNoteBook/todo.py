menu_list = [
    ("Add to-do list", "add_task"),
    ("View to-do list", "view_task"),
    ("Delete to-do list", "delete_task"),
    ("Mark as complete", "mark_as_complete"),
    # "Edit to-do list",
    # "Set due date",
    # "View completed tasks",
    # "Clear all tasks",
    ("Exit", "exit_task"),
]


def mark_as_complete(task_list):
    view_task(task_list)
    task_id = int(input("Enter the task number to complete: "))
    if 1 <= int(task_id) <= len(task_list):
        task_list[task_id - 1][1] = True
        print("Task marked as complete.")
    else:
        print("selected invalid task id")


def delete_task(task_list):

    view_task(task_list)
    task_id = int(input("Enter the task number to delete: "))

    if 1 <= int(task_id) <= len(task_list):
        del task_list[task_id - 1]
        print(f"{task_id} deleted successfully .")
    else:
        print("selected invalid task id")


def exit_task(task_list):
    task_list.clear()


def to_do_menu():
    print("Choose from the options below:")
    for index, (item, _) in enumerate(menu_list, 1):
        print(f"{index}. {item}")


def add_task(task_list):

    tasks = input("Please enter your task: ")
    task_list.append([tasks, False])
    print("Task Added successfully")


def view_task(task_list):
    print("Your task list: ")

    if not task_list:
        print("\nThere are no tasks.")
    else:
        for ids, item in enumerate(task_list, start=1):
            status = "Done" if item[1] else "Not Done"
            print(f"{ids} : {item[0]} - Status : {status} ")


def main():
    task_list = []
    while True:
        to_do_menu()
        choice = input(f"Enter your choice (1-{len(menu_list)}): ")

        if choice.isdigit() and 1 <= int(choice) <= len(menu_list):
            try:
                function_title, function_name = menu_list[int(choice) - 1]

                function = globals()[function_name]
                function(task_list)
            except Exception as error:
                print(
                    f"Error while executing '{menu_list[int(choice) - 1][0]}': {error}"
                )

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
