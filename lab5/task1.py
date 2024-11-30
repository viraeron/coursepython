# TODO Написать 3 класса с документацией и аннотацией типов
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
