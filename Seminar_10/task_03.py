class DataPerson:

    def __init__(self, name: str, sername: str, age: int):
        self.name = name
        self.sername = sername
        self.__age = age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.name}\n {self.sername}\n {self.__age}"

human_1 = DataPerson('Petr', 'Petrov', 27)
human_2 = DataPerson('Sergey', 'Serov', 30)

print(human_1)
print(human_2)