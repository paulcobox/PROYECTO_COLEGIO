import sys
from models.profesor import Profesor


class ProfesorController:
    pass
    def __init__(self):
        self.profesor = Profesor()

    def list_profesores(self):
        profesores = self.profesor.get_profesor_all('ID_PROFESOR')
        print("----------------------------")
        print("ID | NOMBRE | EDAD | CORREO ")
        print("----------------------------")
        for profe in profesores:
            print(profe)

    def list_profesor(self, id):
        profesor_one = self.profesor.get_profesor({'ID_PROFESOR': id})
        return profesor_one

    def list_profesor_columns(self, data):
        profesores = self.profesor.get_profesores_columns(data)
        return profesores

    def insert_profesor(self, data):
        self.profesor.insert_profesor(data)
        print(f'\n ====> Se creo con exito el Profesor {data}<====\n ')
        return True

    def update_profesor(self, id_object, data):
        self.profesor.update_profesor(id_object, data)
        print(f'\n ====> Se actualizo con exito el Profesor con los datos :  {data}<====\n ')
        return True

    def delete_profesor(self, id_object):
        self.profesor.delete_profesor(id_object)
        print(f'\n ====> Se elimino con exito el Profesor de {id_object}<====\n ')
        return True

    



