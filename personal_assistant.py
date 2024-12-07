def main_menu():
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Управление финансовыми записями")
    print("5. Калькулятор")
    print("6. Выход")

main_menu()

import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp

class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump(self.notes, f, indent=4)

    def create_note(self, title, content):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        new_note = Note(note_id, title, content, timestamp)
        self.notes.append(new_note.__dict__)
        self.save_notes()

    def view_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")

# Пример использования
note_manager = NoteManager()
note_manager.create_note("Заметка 1", "Содержимое заметки 1")
note_manager.view_notes()

class Task:
    def __init__(self, task_id, title, description, done=False, priority='Низкий', due_date='01-01-2000'):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, description, priority, due_date):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, priority=priority, due_date=due_date)
        self.tasks.append(new_task.__dict__)
        self.save_tasks()

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Задача 1", "Описание задачи 1", "Высокий", "30-12-2024")
task_manager.view_tasks()

class Contact:
    def __init__(self, contact_id, name, phone='', email=''):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

# Пример использования
contact_manager = ContactManager()
contact_manager.add_contact("Контакт 1", "123456789", "contact1@example.com")
contact_manager.view_contacts()



class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class FinanceManager:
    def __init__(self, filename='finance.json'):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_records(self):
        with open(self.filename, 'w') as f:
            json.dump(self.records, f, indent=4)

# Пример использования
finance_manager = FinanceManager()
finance_manager.add_record(1000.00, "Зарплата", "30-11-2024", "Описание финансовой записи 1")
finance_manager.view_records()


def calculator():
    while True:
        expression = input("Введите выражение для расчета или 'выход' для завершения: ")

        if expression.lower() == 'выход':
            break

        try:
            result = eval(expression)
            print(f"Результат: {result}")

        except ZeroDivisionError:
            print("Ошибка: Деление на ноль.")


calculator()