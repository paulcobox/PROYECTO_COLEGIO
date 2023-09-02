import sys
from models.salon import Salon


class SalonController:
    pass
    def __init__(self):
        self.salon = Salon()

    def list_salones(self):
        salones = self.salon.get_salon_all('ID_SALON')
        print("----------------------------")
        print("ID | NOMBRE ")
        print("----------------------------")
        for salon in salones:
            print(salon)

    def list_salon(self, id):
        salon_one = self.salon.get_salon({'ID_SALON': id})
        return salon_one

    def list_salon_columns(self, data):
        salones = self.salon.get_salones_columns(data)
        return salones

    def insert_salon(self, data):
        self.salon.insert_salon(data)
        print(f'\n ====> Se creo con exito el Salon {data}<====\n ')
        return True

    def update_salon(self, id_object, data):
        self.salon.update_salon(id_object, data)
        print(f'\n ====> Se actualizo con exito el Salon con los datos :  {data}<====\n ')
        return True

    def delete_salon(self, id_object):
        self.salon.delete_salon(id_object)
        print(f'\n ====> Se elimino con exito el Salon de {id_object}<====\n ')
        return True

    



