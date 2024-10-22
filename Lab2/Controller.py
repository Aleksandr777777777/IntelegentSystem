class Controller:
    def __init__(self, elevators):
        self.elevators = elevators  

    def handle_request(self, pickup_floor, target_floor):
        chosen_elevator = self.choose_elevator(pickup_floor)
        self.move_elevator(chosen_elevator, pickup_floor)

        chosen_elevator.open_doors()
        chosen_elevator.close_doors()

        self.move_elevator(chosen_elevator, target_floor)

        chosen_elevator.open_doors()
        chosen_elevator.close_doors()

        return chosen_elevator.movement_count, chosen_elevator

    def choose_elevator(self, pickup_floor):
        """Выбираем ближайший свободный лифт без использования if."""
        elevators_distances = [
            (self.elevators[0], abs(self.elevators[0].current_floor - pickup_floor)),
            (self.elevators[1], abs(self.elevators[1].current_floor - pickup_floor))
        ]

        # Используем list comprehension для фильтрации занятых лифтов
        free_elevators = [elev for elev, distance in elevators_distances if not elev.is_busy()]
        
        # Если есть свободный лифт, выбираем ближайший
        closest_elevator = min(free_elevators, key=lambda elev: abs(elev.current_floor - pickup_floor), default=None)
        
        # Устанавливаем занятость лифта, если он есть
        closest_elevator and closest_elevator.set_busy(True)

        return closest_elevator


    def move_elevator(self, elevator, target_floor):
        """Двигаем лифт до нужного этажа."""
        elevator.set_target(target_floor)
        elevator.execute_movement()