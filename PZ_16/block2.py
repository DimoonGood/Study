#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства "кличка" и "порода".
class Animal:
    def __init__(self, vid, legs, color):
        self.vid = vid
        self.legs = legs
        self.color = color

class Dog(Animal):
    def __init__(self, poroda, name, age, color):
        super().__init__("Собака", 4, color)
        self.poroda = poroda
        self.name = name

dog = Dog("Овчарка", "Шарик", 3, "черный")

print("Вид:", dog.vid)
print("Порода:", dog.poroda)
print("Имя:", dog.name)
print("Цвет шерсти:", dog.color)
print("Количество лап:", dog.legs)