class Transmission:
    """
    Родительский класс с типами передач
        gear_ratio (float): Передаточное число
        efficiency (float): КПД (от 0 до 1).
    """

    def __init__(self, gear_ratio: float, efficiency: float):
        self._gear_ratio = gear_ratio
        self._efficiency = efficiency

    @property
    def gear_ratio(self) -> float:
        # Возвращает передаточное число
        return self._gear_ratio

    @property
    def efficiency(self) -> float:
        # Возвращает КПД
        return self._efficiency

    def calculate_output_torque(self, input_torque: float) -> float:
        """
        Рассчитывает момент на выходном валу основываясь на моменте входного вала

            input_torque (float): Момент на входном валу

        Возвращает момент на выходном валу
        """
        return input_torque * self.gear_ratio * self.efficiency

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(gear_ratio={self.gear_ratio!r}, efficiency={self.efficiency!r})"


class WormGear(Transmission):
    """
    Червячная передача

        lead_angle (float): Угол наклона винтовой линии
	raise ValueError: значения угла не является числом
    """

    def __init__(self, gear_ratio: float, efficiency: float, lead_angle: float):
        super().__init__(gear_ratio, efficiency)
        self.lead_angle = lead_angle

    @property
    def lead_angle(self) -> float:
        # Вовзращает угол наклона винтовой линии
        return self._lead_angle

    @lead_angle.setter
    def lead_angle(self, value: float):
        if not isinstance(value, (float, int)):
            raise ValueError("Значение угла должен быть числом")
        self._lead_angle = float(value)

    def __str__(self) -> str:
        return f"{super().__str__()} с углом равным {self.lead_angle}°"


class CylindricalGear(Transmission):
    """
    Цилиндрическая прямозубая передача

        number_of_teeth (int): Число зубьев
	raise ValueError: если число зубьев != натуральное число
    """

    def __init__(self, gear_ratio: float, efficiency: float, number_of_teeth: int):
        super().__init__(gear_ratio, efficiency)
        self.number_of_teeth = number_of_teeth

    @property
    def number_of_teeth(self) -> int:
        # Возвращает число зубьев
        return self._number_of_teeth

    @number_of_teeth.setter
    def number_of_teeth(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Число зубьев должно быть натуральным числом")
        self._number_of_teeth = value

    def __str__(self) -> str:
        return f"{super().__str__()} with {self.number_of_teeth} teeth"

    def calculate_output_torque(self, input_torque: float) -> float:
        # Расчет КПД
        return super().calculate_output_torque(input_torque)


if __name__ == "__main__":
    print;
