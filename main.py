# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class User:
    def __init__(self, login:str, mail:str, age:int) -> None:
        """
        Создание и подготовка объекта "Пользователь"
        :param login: Логин
        :param mail: Почта
        :param age: Возраст

        Пример:
        >>> user = User("SKZ2017", "skz.2017@mail.ru", 16)
        """
        if not isinstance(login, str):
            raise TypeError("Логин должен быть типа str")
        self.login = login

        if not isinstance(mail, str):
            raise TypeError("Почта должна быть типа str")
        self.mail = mail

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 14:
            raise ValueError("Возраст пользователя не должен быть меньше 14")
        self.age = age

    def new_mail(self) -> str:
        """
        Функция создаёт новую почту
        :return: Новая почта

        Пример:
        >>> user = User("SKZ2017", "skz.2017@mail.ru", 16)
        >>> user.new_mail()
        """
        ...

    def add_friend(self, friend:str) -> None:
        """
        Функция добавляет друга в список друзей
        :param friend: Имя друга
        :return: Возвращает строку 'имя друга' добавлен в друзья

        Пример:
        >>> user = User("SKZ2017", "skz.2017@mail.ru", 16)
        >>> user.add_friend("Bbokari")
        """
        if not isinstance(friend, str):
            raise TypeError("Имя должно быть типа str")
        ...

    def welcome_user(self) -> str:
        """
        Приветствие пользователя
        :return: Выводит строчку с приветствием пользователя

        Пример:
        >>> user = User("SKZ2017", "skz.2017@mail.ru", 16)
        >>> user.welcome_user()
        """
        ...


class Kettle:
    def __init__(self, kettle_volume:int, water_volume:int) -> None:
        """
        Создание и подготовка объекта "Заварочный чайник"
        :param water_volume: Объём воды
        :param kettle_volume: Объём чайника

        Пример:
        >>> kettle = Kettle(250, 175)
        """
        if not isinstance(kettle_volume, (int, float)):
            raise TypeError("Объём чайника должен быть типа int или float")
        if kettle_volume <= 0:
            raise ValueError("Объём чайника должен быть положительным числом")
        self.kettle_volume = kettle_volume

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Объём воды должен быть типа int или float")
        if water_volume < 0:
            raise ValueError("Объём воды не должно быть отрицательным числом")
        self.water_volume = water_volume

    def pour_water(self):
        """
        Налить воду в чайник
        :raise ValueError: Количество воды не должно превышать объём чайника

        Пример:
        >>> kettle = Kettle(250, 175)
        >>> kettle.pour_water()
        """
        ...

    def pour_out_water (self, sheer_volume:int) -> None:
        """
        Выливает воду из чайника
        :param sheer_volume: Объём вылитой воды
        :raise ValueError: Количество выливаемой воды не должно превышать объём воды
        :return: Объём вылитой воды

        Пример:
        >>> kettle = Kettle(250, 175)
        >>> kettle.pour_out_water(80)
        """
        ...


class Phone:
    def __init__(self, brand:str, model:str, charge:int) -> None:
        """
        Создание и подготовка объекта "Телефон"
        :param brand: Xiaomi
        :param model: Redmi Note 10T
        :param charge: 73

        Пример:
        >>> phone = Phone("Xiaomi", "Redmi Note 10T", 73)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка телефона должна быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть типа str")
        self.model = model

        if not isinstance(charge, int):
            raise TypeError("Заряд телефона должна быть типа int")
        if charge < 0:
            raise ValueError("Заряд не может быть отрицательным числом")
        if charge > 100:
            raise ValueError("Заряд не может быть больше 100")
        self.charge = charge

    def charge_the_phone(self):
        """
        Зарядить телефон
        :raise ValueError: Если заряд телефона превышает 100, то возвращается ошибка

        Пример:
        >>> phone = Phone("Xiaomi", "Redmi Note 10T", 73)
        >>> phone.charge_the_phone()
        """
        ...

    def telephone_information(self):
        """
        Посмотреть информацию о телефоне
        :return: Выводит марку и модель телефона

        Пример:
        >>> phone = Phone("Xiaomi", "Redmi Note 10T", 73)
        >>> phone.telephone_information()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
