if __name__ == "__main__":
    class Transmission:

        def __init__(self, gear_ratio: float, efficiency: float):
            """
            :param gear_ratio: Передаточное отношение передачи.
            :param efficiency: Эффективность передачи (в диапазоне от 0 до 1).
            """
            self._gear_ratio = gear_ratio
            self._efficiency = efficiency

        @property
        def gear_ratio(self) -> float:
            #Передатьчное отношение
            return self._gear_ratio

        @property
        def efficiency(self) -> float:
            #КПД
            return self._efficiency


        def __repr__(self) -> str:

            return f"{self.__class__.__name__}(gear_ratio={self.gear_ratio!r}, efficiency={self.efficiency!r})"


    class WormGear(Transmission):
        #червячная передача

        def __init__(self, gear_ratio: float, efficiency: float, lead_angle: float):

            super().__init__(gear_ratio, efficiency)
            self.lead_angle = lead_angle

        @property
        def lead_angle(self) -> float:
            #Угол подъема
            return self._lead_angle

        @lead_angle.setter
        def lead_angle(self, value: float):
            if not isinstance(value, (float, int)):
                raise ValueError("Угол подъема должен быть числом.")
            self._lead_angle = float(value)

        def __str__(self) -> str:
            return f"{super().__str__()} с углом подъема {self.lead_angle}°"

        def calculate_output_torque(self, input_torque: float) -> float:
            #Момент
            return input_torque
            self.gear_ratio
            self.efficiency


    class CylindricalGear(Transmission):

        def __init__(self, gear_ratio: float, efficiency: float, number_of_teeth: int):

            super().__init__(gear_ratio, efficiency)
            self.number_of_teeth = number_of_teeth

        @property
        def number_of_teeth(self) -> int:
            return self._number_of_teeth

        @number_of_teeth.setter
        def number_of_teeth(self, value: int):
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Количество зубьев должно быть положительным целым числом.")
            self._number_of_teeth = value

        def __str__(self) -> str:
            return f"{super().__str__()} с {self.number_of_teeth} зубьями"


    pass
