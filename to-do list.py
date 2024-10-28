import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, title, description):
        self.tasks[index].title = title
        self.tasks[index].description = description

    def delete_task(self, index):
        del self.tasks[index]

    def mark_complete(self, index):
        self.tasks[index].completed = True

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(**task) for task in task_list]
        except FileNotFoundError:
            pass  # No file to load

def main():
    todo_list = ToDoList()
    todo_list.load_from_file('tasks.json')

    while True:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list.tasks):
            status = "✓" if task.completed else "✗"
            print(f"{idx + 1}. [{status}] {task.title}: {task.description}")

        print("\nOptions: [1] Add [2] Update [3] Delete [4] Complete [5] Save [6] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            description = input("Task description: ")
            todo_list.add_task(Task(title, description))
        elif choice == '2':
            index = int(input("Task number to update: ")) - 1
            title = input("New title: ")
            description = input("New description: ")
            todo_list.update_task(index, title, description)
        elif choice == '3':
            index = int(input("Task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Task number to complete: ")) - 1
            todo_list.mark_complete(index)
        elif choice == '5':
            todo_list.save_to_file('tasks.json')
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
