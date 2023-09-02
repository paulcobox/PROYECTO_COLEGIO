import sys
from models.alumno import Alumno


class AlumnoController:
    pass
    def __init__(self):
        self.alumno = Alumno()

    def list_alumnos(self):
        alumnos = self.alumno.get_alumno_all('ID_ALUMNO')
        print("----------------------------")
        print("NOMBRE | EDAD | ID | CORREO")
        print("----------------------------")
        for alum in alumnos:
            print(alum)

    def list_alumno(self, id):
        alumno_one = self.alumno.get_alumno({'ID_ALUMNO': id})
        return alumno_one

    def list_alumno_columns(self, data):
        alumnos = self.alumno.get_alumnos_columns(data)
        return alumnos

    def insert_alumno(self, data):
        self.alumno.insert_alumno(data)
        print(f'\n ====> Se creo con exito el Alumno {data}<====\n ')
        return True

    def update_alumno(self, id_object, data):
        self.alumno.update_alumno(id_object, data)
        print(f'\n ====> Se actualizo con exito el Alumno con los datos :  {data}<====\n ')
        return True

    def delete_alumno(self, id_object):
        self.alumno.delete_alumno(id_object)
        print(f'\n ====> Se elimino con exito el Alumno de {id_object}<====\n ')
        return True

    



