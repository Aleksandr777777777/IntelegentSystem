from Elevator import Elevator
from Controller import Controller

class Building:
    def __init__(self, num_floors, elevators_positions):
        self.num_floors = num_floors
        self.floor_dispatcher = FloorDispatcher(num_floors)  # Создаем диспетчер этажей
        self.elevators = [Elevator(pos, self.floor_dispatcher) for pos in elevators_positions]
        self.controller = Controller(self.elevators)

    def process_request(self, pickup_floor, target_floor):
        moves, elevator = self.controller.handle_request(pickup_floor, target_floor)
        return moves, elevator


class InvalidFloorError(Exception):
    """Исключение для недопустимых этажей."""
    pass


class FloorDispatcher:
    def __init__(self, max_floor):
        self.valid_floors = {floor: floor for floor in range(1, max_floor + 1)}

    def get_floor(self, floor):
        """Возвращает этаж или вызывает исключение при недопустимом этаже."""
        try:
            return self.valid_floors[floor]  # Если этаж недопустим, KeyError вызовет исключение
        except KeyError:
            raise InvalidFloorError(f"Этаж {floor} недопустим.")
