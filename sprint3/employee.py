class Employee:
    vacation_days = 28
    remaining_vacation_days = vacation_days

    def __init__(self, first_name, second_name, gender) -> None:
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, str_date, days):
        return f"Начало неоплачиваемого отпуска: {str_date}, продолжительность: {days} дней."


class PartTimeEmployee(Employee):
    vacation_days = 14
    remaining_vacation_days = vacation_days

    def __init__(self, first_name, second_name, gender) -> None:
        super().__init__(first_name, second_name, gender)


# Пример использования:
full_time_employee = FullTimeEmployee("Роберт", "Крузо", "м")
print(full_time_employee.get_unpaid_vacation("2023-07-01", 5))
part_time_employee = PartTimeEmployee("Алёна", "Пятницкая", "ж")
print(part_time_employee.get_vacation_details())
print(part_time_employee.remaining_vacation_days)
