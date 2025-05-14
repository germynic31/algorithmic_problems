from datetime import datetime
import json
import os
import sys


class TODO:
    DATETIME_FORMAT = '%d.%m.%Y %H:%M'

    def __init__(self, tasks: list | None = None):
        self.tasks = tasks
        self._create_file()

    def _create_file(self):
        if not os.path.exists('TODO.json') or os.path.getsize('TODO.json') == 0:
            with open('TODO.json', 'w') as f:
                f.write('[]')
            self.tasks = []
        else:
            with open('TODO.json', 'r') as f:
                self.tasks = json.load(f)

    def add_task(self, task):
        task = {
            'task': task,
            'done': False,
            'created': datetime.now().strftime(self.DATETIME_FORMAT),
            'close': None
        }

        self.tasks.append(task)
        with open('TODO.json', 'w') as f:
            json.dump(self.tasks, f)

    def get_tasks(self):
        return self.tasks

    def close_task(self, task_name):
        for task in self.tasks:
            if task['task'] == task_name:
                task['done'] = True
                task['close'] = datetime.now().strftime(self.DATETIME_FORMAT)
        with open('TODO.json', 'w') as f:
            json.dump(self.tasks, f)

    def delete_task(self, task_name):
        for task in self.tasks:
            if task['task'] == task_name:
                self.tasks.remove(task)
        with open('TODO.json', 'w') as f:
            json.dump(self.tasks, f)

    def exit_program(self):
        print('Exiting program...')
        sys.exit(0)


def main():
    todo = TODO()
    start_message = (
        'TODO LIST:\n'
        '1. Add task\n'
        '2. Get tasks\n'
        '3. Close task\n'
        '4. Delete task\n'
        '5. Repeat start message\n'
        '6. Exit'
    )
    print(start_message)
    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            task = input('Enter task: ')
            todo.add_task(task)
        elif choice == 2:
            print(todo.get_tasks())
        elif choice == 3:
            task = input('Enter task: ')
            todo.close_task(task)
        elif choice == 4:
            task = input('Enter task: ')
            todo.delete_task(task)
        elif choice == 5:
            print(start_message)
        elif choice == 6:
            todo.exit_program()
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
