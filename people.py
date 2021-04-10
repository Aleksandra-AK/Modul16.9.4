class People:
    def __init__(self, name, town):
        self.name = name
        self.town = town

    def get_guest(self):
        return f'Гость: {self.name}, {self.town}'


class Volunteers(People):
    def __init__(self, name, town, status):
        super().__init__(name, town)
        self.status = status

    def get_guest(self):
        return f'Гость-волонтер: {self.name}, {self.town}, {self.status}'


class Worker(People):
    def __init__(self, name, town, position):
        super().__init__(name, town)
        self.position = position

    def get_guest(self):
        return f'Сотрудник компании: {self.name}, {self.town}, {self.position}'


if __name__ == "__main__":
    people = People("Ivan Sidorov", "Moscow")
    volunteer = Volunteers("Denis Komov", "Novosibirsk", "Dog keeper")
    worker = Worker("Dusa Muhina", "Rostov", "Developer")
    print(people.get_guest(), volunteer.get_guest(), worker.get_guest(), sep="\n")
