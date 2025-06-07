#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для проверки на високосный год и определения количества дней в месяце.
class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def visokosniy_year(self):
        return self.year % 4 == 0

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.visokosniy_year() else 28
        else:
            return "Неверный месяц"


calendar = Calendar(2024, 15, 29)
print("Високосный год:", calendar.visokosniy_year())
print("Дней в месяце:", calendar.days_in_month())