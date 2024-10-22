from Building import Building

if __name__ == "__main__":
    num_floors = 10
    elevators_positions = [1, 5]  
    
    building = Building(num_floors, elevators_positions)
    
    requests = [(1, 10), (8, 1)] 
    
    for request in requests:
        pickup_floor, target_floor = request
        moves, chosen_elevator = building.process_request(pickup_floor, target_floor)
        print(f"Лифт переместился {moves} раз(а) до открытия дверей на этаже {target_floor}")
        print("Лог команд лифта:")
        print(chosen_elevator.get_commands())
        print()  

    for idx, elevator in enumerate(building.elevators):
        print(f"\nЛог команд лифта {idx + 1}:")
        print(elevator.get_commands())