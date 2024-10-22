class Elevator:
    def __init__(self, current_floor, floor_dispatcher):
        self.current_floor = current_floor
        self.floor_dispatcher = floor_dispatcher  
        self.movement_count = 0
        self.command_log = []
        self.busy = False
        self.direction = None
        self.target_floor = None
        
        self.movement_actions = {
            'up': self.move_up,
            'down': self.move_down
        }

    def set_target(self, target_floor):
        """Устанавливаем целевой этаж, проверяем его через FloorDispatcher, и рассчитываем направление."""
        self.target_floor = self.floor_dispatcher.get_floor(target_floor)  # Проверка допустимости этажа
        self.direction = 'up' if self.current_floor < self.target_floor else 'down'

    def move_up(self):
        next_floor = self.current_floor + 1
        self.current_floor = self.floor_dispatcher.get_floor(next_floor)  # Проверка через диспетчер
        self.movement_count += 1
        self.command_log.append(f"Подняться на {self.current_floor}")

    def move_down(self):
        next_floor = self.current_floor - 1
        self.current_floor = self.floor_dispatcher.get_floor(next_floor) 
        self.movement_count += 1
        self.command_log.append(f"Опуститься на {self.current_floor}")

    def open_doors(self):
        self.command_log.append(f"Открыть двери на {self.current_floor}")

    def close_doors(self):
        self.command_log.append("Закрыть двери")

    def execute_movement(self):
        """Выполняем движение лифта на целевой этаж."""
        while self.current_floor != self.target_floor:
            self.movement_actions[self.direction]()

    def get_commands(self):
        return "\n".join(self.command_log)

    def is_busy(self):
        return self.busy

    def set_busy(self, state):
        self.busy = state
