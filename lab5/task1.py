# TODO Написать 3 класса с документацией и аннотацией типов
class Motorcycle:
    def __init__(self, make: str, model: str, engine: Engine):
        """
        Создание и подготовка к работе объекта "Мотоцикл".

        :param make: Производитель мотоцикла.
        :param model: Модель мотоцикла.
        :param engine: Двигатель мотоцикла (объект класса Engine или ElectricEngine).

        Примеры:
        >>> engine = Engine(100, 1.2, 'бензин')
        >>> motorcycle = Motorcycle('Yamaha', 'YZF-R3', engine)  # инициализация экземпляра класса
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой.")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой.")
        if not isinstance(engine, (Engine, ElectricEngine)):
            raise TypeError("Двигатель должен быть объектом класса Engine или ElectricEngine.")

        self.make = make
        self.model = model
        self.engine = engine

    def start(self) -> str:
        """
        Метод для запуска мотоцикла.

        :return: Сообщение о запуске мотоцикла.

        Примеры:
        >>> engine = Engine(100, 1.2, 'бензин')
        >>> motorcycle = Motorcycle('Yamaha', 'YZF-R3', engine)
        >>> motorcycle.start()  # вывод сообщения о запуске
        'Мотоцикл Yamaha YZF-R3 запущен.'
        """
        return f"Мотоцикл {self.make} {self.model} запущен."

    def stop(self) -> str:
        """
        Метод для остановки мотоцикла.

        :return: Сообщение о остановке мотоцикла.

        Примеры:
        >>> engine = Engine(100, 1.2, 'бензин')
        >>> motorcycle = Motorcycle('Yamaha', 'YZF-R3', engine)
        >>> motorcycle.stop()  # вывод сообщения о остановке
        'Мотоцикл Yamaha YZF-R3 остановлен.'
        """
        return f"Мотоцикл {self.make} {self.model} остановлен."

    def get_motorcycle_specifications(self) -> str:
        """
        Метод для получения характеристик мотоцикла.

        :return: Строка с характеристиками мотоцикла.

        Примеры:
        >>> engine = Engine(100, 1.2, 'бензин')
        >>> motorcycle = Motorcycle('Yamaha', 'YZF-R3', engine)
        >>> motorcycle.get_motorcycle_specifications()
        'Производитель: Yamaha, Модель: YZF-R3, Характеристики двигателя: Мощность: 100 л.с., Объем: 1.2 л, Тип топлива: бензин.'
        """
        engine_specs = self.engine.get_engine_specifications()
        return f"Производитель: {self.make}, Модель: {self.model}, Характеристики двигателя: {engine_specs}."
class ElectricEngine:
    def __init__(self, power: float, battery_capacity: float):
        """
        Создание и подготовка к работе объекта "Электрический двигатель".

        :param power: Мощность двигателя в киловаттах.
        :param battery_capacity: Вместимость батареи в киловатт-часах.

        Примеры:
        >>> electric_engine = ElectricEngine(100, 50)  # инициализация экземпляра класса
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должна быть типа int или float.")
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом.")

        if not isinstance(battery_capacity, (int, float)):
            raise TypeError("Вместимость батареи должна быть типа int или float.")
        if battery_capacity <= 0:
            raise ValueError("Вместимость батареи должна быть положительным числом.")

        self.power = power
        self.battery_capacity = battery_capacity

    def start(self) -> str:
        """
        Метод для запуска электрического двигателя.

        :return: Сообщение о запуске двигателя.

        Примеры:
        >>> electric_engine = ElectricEngine(100, 50)
        >>> electric_engine.start()  # вывод сообщения о запуске
        'Электрический двигатель запущен.'
        """
        return "Электрический двигатель запущен."

    def stop(self) -> str:
        """
        Метод для остановки электрического двигателя.

        :return: Сообщение о остановке двигателя.

        Примеры:
        >>> electric_engine = ElectricEngine(100, 50)
        >>> electric_engine.stop()  # вывод сообщения о остановке
        'Электрический двигатель остановлен.'
        """
        return "Электрический двигатель остановлен."

    def get_engine_specifications(self) -> str:
        """
        Метод для получения характеристик электрического двигателя.

        :return: Строка с характеристиками двигателя.

        Примеры:
        >>> electric_engine = ElectricEngine(100, 50)
        >>> electric_engine.get_engine_specifications()
        'Мощность: 100 кВт, Вместимость батареи: 50 кВтч.'
        """
        return f"Мощность: {self.power} кВт, Вместимость батареи: {self.battery_capacity} кВтч."
class Engine:
    def __init__(self, horsepower: float, displacement: float, fuel_type: str):
        """
        Создание и подготовка к работе объекта "Двигатель внутреннего сгорания".

        :param horsepower: Мощность двигателя в лошадиных силах.
        :param displacement: Объем двигателя в литрах.
        :param fuel_type: Тип топлива, используемого двигателем (например, 'бензин', 'дизель').

        Примеры:
        >>> engine = InternalCombustionEngine(150, 2.0, 'бензин')  # инициализация экземпляра класса
        """
        if not isinstance(horsepower, (int, float)):
            raise TypeError("Мощность должна быть типа int или float.")
        if horsepower <= 0:
            raise ValueError("Мощность должна быть положительным числом.")

        if not isinstance(displacement, (int, float)):
            raise TypeError("Объем двигателя должен быть типа int или float.")
        if displacement <= 0:
            raise ValueError("Объем двигателя должен быть положительным числом.")

        if not isinstance(fuel_type, str):
            raise TypeError("Тип топлива должен быть строкой.")

        self.horsepower = horsepower
        self.displacement = displacement
        self.fuel_type = fuel_type

    def start(self) -> str:
        """
        Метод для запуска двигателя.

        :return: Сообщение о запуске двигателя.

        Примеры:
        >>> engine = InternalCombustionEngine(150, 2.0, 'бензин')
        >>> engine.start()  # вывод сообщения о запуске
        'Двигатель запущен.'
        """
        return "Двигатель запущен."

    def stop(self) -> str:
        """
        Метод для остановки двигателя.

        :return: Сообщение о остановке двигателя.

        Примеры:
        >>> engine = InternalCombustionEngine(150, 2.0, 'бензин')
        >>> engine.stop()  # вывод сообщения о остановке
        'Двигатель остановлен.'
        """
        return "Двигатель остановлен."

    def get_engine_specifications(self) -> str:
        """
        Метод для получения характеристик двигателя.

        :return: Строка с характеристиками двигателя.

        Примеры:
        >>> engine = InternalCombustionEngine(150, 2.0, 'бензин')
        >>> engine.get_engine_specifications()
        'Мощность: 150 л.с., Объем: 2.0 л, Тип топлива: бензин.'
        """
        return f"Мощность: {self.horsepower} л.с., Объем: {self.displacement} л, Тип топлива: {self.fuel_type}."
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
