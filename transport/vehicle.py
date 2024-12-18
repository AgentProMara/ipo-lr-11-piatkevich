import uuid
from .client import Client

class Vehicle:
    def __init__(self, capacity):
        if isinstance(capacity, (int, float)) and capacity > 0:
            self.vehicle_id = str(uuid.uuid4())
            self.capacity = capacity
            self.current_load = 0
            self.clients_list = []
        else:
            raise ValueError("Грузоподъемность должна быть положительным числом!")

    def can_load(self, client):
        if isinstance(client.cargo_weight, (int, float)) and client.cargo_weight > 0:
            return self.current_load + client.cargo_weight <= self.capacity
        else:
            raise ValueError("Вес груза клиента должен быть положительным числом!")

    def load_cargo(self, client):
        if self.can_load(client):
            self.current_load += client.cargo_weight
            self.clients_list.append(client)
            return True
        return False

    def __str__(self):
        return f"ID транспорта:{self.vehicle_id},грузоподъёмность:{self.capacity},текущая загрузка:{self.current_load}"
       
class Ship(Vehicle):
    def __init__(self, capacity, name):
        super().__init__(capacity)
        self.name = name

class Truck(Vehicle):
    def __init__(self, capacity, color):
        super().__init__(capacity)
        self.color = color