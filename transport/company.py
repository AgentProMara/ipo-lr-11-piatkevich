class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []  # Список транспортных средств
        self.clients = []   # Список клиентов

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_client(self, client):
        self.clients.append(client)

    def distribute_cargo(self):
        # Распределяем грузы между транспортными средствами
        for client in self.clients:
            remaining_cargo = client.cargo_weight
            for vehicle in self.vehicles:
                available_capacity = vehicle.capacity - vehicle.current_load
                if available_capacity > 0:
                    load_to_add = min(remaining_cargo, available_capacity)
                    vehicle.current_load += load_to_add
                    remaining_cargo -= load_to_add

                if remaining_cargo <= 0:
                    break

            if remaining_cargo > 0:
                print(f"Клиент {client.name} имеет необработанный груз: {remaining_cargo} тонн.")