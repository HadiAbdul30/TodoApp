from tasks import TodoApp

tasks = []
my_app = TodoApp(tasks)
def main():
    my_app.load_tasks()

    while True:
        print("\nWelcome to To-Do App!\n")
        print("1. Add task" \
        "\n2. View tasks" \
        "\n3. Mark as completed" \
        "\n4. Remove task" \
        "\n5. Edit task" \
        "\n6. Do random task" \
        "\n7. Set the prority" \
        "\n8. Search task" \
        "\n9. Exit")
        try:
            choice = int(input("\nChoose an operation from the above by entering number from (1-9): "))
            if choice in range(1, 10):
                if choice == 1:
                    task_name = input("\nAdd a task").strip()
                    my_app.add_task(task_name)
                    my_app.save_task()
                elif choice == 2:
                    my_app.view_tasks()
                elif choice == 3:
                    my_app.mark_as_completed()
                    my_app.save_task()
                elif choice == 4:
                    my_app.remove_task()
                    my_app.save_task()
                elif choice == 5:
                    my_app.edit_task()
                    my_app.save_task()
                elif choice == 6:
                    my_app.do_random_task()
                elif choice == 7:
                    my_app.set_priority()
                    my_app.ave_task()
                elif choice == 8:
                    my_app.search_task()
                elif choice == 9:
                    print("Thanks for using our app!")
                    break   
            else:
                print("\nOnly from 1 to 9!")
        except ValueError:
            print("\nOnly enter numbers! Please")

main()