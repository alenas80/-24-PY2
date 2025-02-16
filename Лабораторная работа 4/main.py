class Feline:
    """
    Базовый класс кошачьи
    :param breed: порода кошки
    :param size: размер кошки(большой, средний, маленький)
    """
    def __init__(self, breed: str, size: str):
        self.__breed = breed
        self.__size = size

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed: str) -> None:
        self.__breed = breed

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str) -> None:
        self.__size = size


    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса
        :return: str
        """
        return f"Порода {self.breed}. Размер {self.size}"

    def __repr__(self) -> str:
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса
        :return: str
        """
        return f"{self.__class__.__name__}(breed={self.breed!r}, size={self.size!r})"

    def eat(self, food_type: str, meal_size: str) -> None:
        """
        Позволяет кошке поесть в зависимости от типа еды и размера порции
        :param food_type: тип еды, которой питается кошка (например, сухой корм, мясо, рыба)
        :param meal_size: размер порции (большой, средний, маленький)
        :return: Возвращает тип еды и размер порции
        """
    ...

    def sleep(self, duration: int, location: str) -> None:
        """
        Имитирует сон кошки
        :param duration: продолжительность сна
        :param location: место сна(диван, кровать, дерево)
        :return: Возвращает продолжительность и место сна
        """
    ...

class WildCat(Feline):
    """
    Дочерний класс дикие кошки
    :param habitat: ареал обитания(лес, саванна)
    """
    def __init__(self, breed: str, size: str, habitat: str):
        super().__init__(breed, size)
        self.habitat = habitat

    def __repr__(self):
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса

        :return: str
        """
        return f"{self.__class__.__name__}(breed={self.breed!r}, size={self.size!r}, habitat={self.habitat!r})"

    def hunting(self, type_prey: str, method: str) -> None:
        """
        Дикой кошке сначала надо поохотится прежде, чем поесть. Поэтому перегружаем метод из базового класса
        :param type_prey: тип добычи
        :param method: метод охоты(погоня, засада)
        :return: тип добычи и как её поймали
        """

class DomesticCat(Feline):
    """
    Дочерний класс домашние кошки
    :param name: кличка кошки
    """
    def __init__(self, breed: str, size: str, name: str):
        super().__init__(breed, size)
        self.name = name

    def __repr__(self):
        """
        Определяет поведение функции repr(), вызванной для экземпляра класса
        :return: str
        """
        return f"{self.__class__.__name__}(breed={self.breed!r}, size={self.size!r}, name={self.name!r})"

    def ask_for_food(self, meow_duration: int) -> None:
        """
        Домашняя кошка просит еду, когда голодна. Поэтому перегружаем метод из базового класса
        :param meow_duration: продолжительность мяуканья, когда кошка просит еду
        :return: продолжительность мяуканья
        """

if __name__ == "__main__":
    # Write your solution here
    pass
