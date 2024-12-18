from transport import Client,Vehicle,TransportCompany,Ship,Truck

def menu():
    company = TransportCompany("TransCo")

    while True:
      print("\nЧто вы хотите сделать?")
      print("1. Добавить клиента")
      print("2. Добавить транспортное средство")
      print("3. Показать все транспортные средства")
      print("4. Распределить грузы")
      print("5. Показать результат распределения")
      print("6. Выйти из программы")

      res = input("\nВыберите пункт из предложенного списка: ")

      if res=="1":
         name=input("Введите имя клиента:")
         weight=float(input("Введите вес груза:"))
         is_vip=input("Клиент VIP?(Да/Нет):").strip().lower()=='да'
         company.add_client(Client(name, weight, is_vip))
         
      elif res=="2":
         type_vehicle=input("Выберите вид транспорта(1-корабль,2-грузовик):")
         capacity=float(input("Введите грузоподъёмность: "))
         if type_vehicle=="1":
            name=input("Введите название судна:")
            company.add_vehicle(Ship(capacity,name))
             
         elif type_vehicle=="2":
            color=input("Введите цвет грузовика:")
            company.add_vehicle(Truck(capacity,color))
         else:
            print("Введен неправильный тип транспорта")

      elif res=="3":
         print("\nТранспортные средства:")
         for vehicle in company.list_vehicles():
            print(vehicle)

      elif res=="4":
         company.optimize_cargo_distribution()
         print("Грузы успешно распределены!")

      elif res=="5":
         print("\nРезультат распределения груза:")
         for vehicle in company.vehicles:
            print(vehicle)
            for client in vehicle.clients_list:
                    print(f" - {client.name}: {client.cargo_weight} тонн, VIP: {'да' if client.is_vip else 'нет'}")
    
      elif res=="6":
         break
      
      else:
         print("Неправильный выбор, попробуйте снова")

if __name__ == "__main__":
    menu()