class Client():
    
    def __init__(self, name,cargo_weight,is_vip=False):
        if isinstance(cargo_weight, (int, float)) and cargo_weight > 0:
            self.name = name
            self.cargo_weight = cargo_weight
            self.is_vip = is_vip
        else:
            raise ValueError("Вес груза должно быть положительным числом!")
            