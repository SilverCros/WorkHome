import json

class Employee:
    def __init__(self, surname, age):
        self.surname = surname
        self.age = age

    def to_dict(self):
        return {'surname': self.surname, 'age': self.age}

    @staticmethod
    def from_dict(data):
        return Employee(data['surname'], data['age'])

class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def load_employees(self, filename):
        try:
            with open(filename, 'r') as file:
                self.employees = [Employee.from_dict(emp) for emp in json.load(file)]
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустого списка сотрудников.")
        except json.JSONDecodeError:
            print("Ошибка при загрузке данных из файла.")

    def save_employees(self, filename):
        with open(filename, 'w') as file:
            json.dump([emp.to_dict() for emp in self.employees], file)

    def add_employee(self, surname, age):
        self.employees.append(Employee(surname, age))

    def edit_employee(self, surname, new_surname, new_age):
        for emp in self.employees:
            if emp.surname == surname:
                emp.surname = new_surname
                emp.age = new_age
                return
        print("Сотрудник не найден.")

    def delete_employee(self, surname):
        self.employees = [emp for emp in self.employees if emp.surname != surname]

    def find_employee_by_surname(self, surname):
        return [emp for emp in self.employees if emp.surname == surname]

    def find_employees_by_age(self, age):
        return [emp for emp in self.employees if emp.age == age]

    def find_employees_by_initial(self, initial):
        return [emp for emp in self.employees if emp.surname.startswith(initial)]

    def display_employees(self):
        for emp in self.employees:
            print(f"Фамилия: {emp.surname}, Возраст: {emp.age}")

def main():
    system = EmployeeSystem()
    filename = input("Введите имя файла для загрузки сотрудников: ")
    system.load_employees(filename)

    while True:
        print("\n1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Найти сотрудника по фамилии")
        print("5. Найти сотрудников по возрасту")
        print("6. Найти сотрудников по первой букве фамилии")
        print("7. Вывести всех сотрудников")
        print("8. Сохранить сотрудников в файл")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            surname = input("Введите фамилию: ")
            age = int(input("Введите возраст: "))
            system.add_employee(surname, age)
        elif choice == '2':
            surname = input("Введите фамилию сотрудника для редактирования: ")
            new_surname = input("Введите новую фамилию: ")
            new_age = int(input("Введите новый возраст: "))
            system.edit_employee(surname, new_surname, new_age)
        elif choice == '3':
            surname = input("Введите фамилию сотрудника для удаления: ")
            system.delete_employee(surname)
        elif choice == '4':
            surname = input("Введите фамилию для поиска: ")
            found = system.find_employee_by_surname(surname)
            if found:
                for emp in found:
                    print(f"Найден: Фамилия: {emp.surname}, Возраст: {emp.age}")
            else:
                print("Сотрудник не найден.")
        elif choice == '5':
            age = int(input("Введите возраст для поиска: "))
            found = system.find_employees_by_age(age)
            if found:
                for emp in found:
                    print(f"Найден: Фамилия: {emp.surname}, Возраст: {emp.age}")
            else:
                print("Сотрудники не найдены.")
        elif choice == '6':
            initial = input("Введите первую букву фамилии: ")
            found = system.find_employees_by_initial(initial)
            if found:
                for emp in found:
                    print(f"Найден: Фамилия: {emp.surname}, Возраст: {emp.age}")
            else:
                print("Сотрудники не найдены.")
        elif choice == '7':
            system.display_employees()
        elif choice == '8':
            filename = input("Введите имя файла для сохранения сотрудников: ")
            system.save_employees(filename)
            print("Сотрудники сохранены.")
        elif choice == '9':
            filename = input("Введите имя файла для сохранения сотрудников перед выходом: ")
            system.save_employees(filename)
            print("Сотрудники сохранены. Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()