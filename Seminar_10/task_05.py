class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: float | int):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float | int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name: str, weight: float | int):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'


if __name__ == '__main__':
    b = Bird('Bird1', 2.5)
    f = Fish('Fish1', 2.5)
    m = Mammal('Mammal1', 2.5)

    print(f'{b.wing_length()=}')
    print(f'{f.depth()=}')
    print(f'{m.category()=}')