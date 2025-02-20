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
    # Нельзя изменить породу кошки

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str) -> None:
        self.__size = size
    # Неизменяемая характеристика кошки(Большая кошка не может стать маленькой)

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

    def eat(self, meal_size:str, food_type:str="обычная еда") -> None:
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

    def eat(self, meal_size:str, food_type:str="сырое мясо") -> None:
        """
        Дикой кошке охотится на добычу и ест пойманную добычу. Поэтому перегружаем метод из базового класса
        :param meal_size: размер порции (большой, средний, маленький)
        :param food_type: тип добычи
        :return: тип добычи и размер порции
        """
        super().eat(food_type, meal_size)

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

    def eat(self, meal_size:str, food_type:str="кошачий корм") -> None:
        """
        Домашняя кошка просит еду и ест, то что даст хозяин. Поэтому перегружаем метод из базового класса
        :param food_type: тип корма
        :param meal_size: размер порции (большой, средний, маленький)
        :return: тип корма и размер порции
        """
        super().eat(food_type, meal_size)

if __name__ == "__main__":
    # Write your solution here
    pass
