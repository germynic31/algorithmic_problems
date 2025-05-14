from datetime import datetime
import json
import os
import sys


class TODO:
    DATETIME_FORMAT = '%d.%m.%Y %H:%M'
    FILE_NAME = 'TODO.json'

    def __init__(self):
        self.tasks = []
        self._initialize_file()

    def _initialize_file(self):
        """Инициализирует файл задач, создает если не существует"""
        try:
            if (
                not os.path.exists(self.FILE_NAME) or
                os.path.getsize(self.FILE_NAME) == 0
            ):
                self._save_tasks()
            else:
                with open(self.FILE_NAME, 'r') as f:
                    self.tasks = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
            self._save_tasks()

    def _save_tasks(self):
        """Сохраняет задачи в файл"""
        try:
            with open(self.FILE_NAME, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, task_description: str):
        """Добавляет новую задачу"""
        new_task = {
            'task': task_description,
            'done': False,
            'created': datetime.now().strftime(self.DATETIME_FORMAT),
            'completed': None
        }
        self.tasks.append(new_task)
        self._save_tasks()

    def get_tasks(self) -> list:
        """Возвращает список всех задач"""
        return self.tasks

    def complete_task(self, task_description: str):
        """Отмечает задачу как выполненную"""
        for task in self.tasks:
            if task['task'] == task_description:
                task['done'] = True
                task['completed'] = datetime.now().strftime(self.DATETIME_FORMAT)
                self._save_tasks()
                return
        print(f"Task '{task_description}' not found")

    def delete_task(self, task_description: str):
        """Удаляет задачу"""
        self.tasks = [task for task in self.tasks if task['task'] != task_description]
        self._save_tasks()

    @staticmethod
    def exit_program():
        """Завершает программу"""
        print('Exiting program...')
        sys.exit(0)


def display_menu():
    """Отображает меню пользователя"""
    menu = """
    TODO LIST:
    1. Add task
    2. Show all tasks
    3. Complete task
    4. Delete task
    5. Show menu again
    6. Exit
    """
    print(menu)


def main():
    todo = TODO()
    display_menu()

    while True:
        try:
            choice = input('\nEnter your choice (1-6): ').strip()

            if choice == '1':
                task = input('Enter task description: ').strip()
                if task:
                    todo.add_task(task)
                else:
                    print("Task description cannot be empty")
            elif choice == '2':
                tasks = todo.get_tasks()
                if tasks:
                    for idx, task in enumerate(tasks, 1):
                        status = "✓" if task['done'] else "✗"
                        print(f"{idx}. [{status}] {task['task']} (Created: {task['created']})")
                else:
                    print("No tasks found")
            elif choice == '3':
                task = input('Enter task description to complete: ').strip()
                todo.complete_task(task)
            elif choice == '4':
                task = input('Enter task description to delete: ').strip()
                todo.delete_task(task)
            elif choice == '5':
                display_menu()
            elif choice == '6':
                todo.exit_program()
            else:
                print("Invalid choice. Please enter a number from 1 to 6")

        except KeyboardInterrupt:
            todo.exit_program()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()