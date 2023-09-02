import sys
from models.curso import Curso


class CursoController:
    pass
    def __init__(self):
        self.curso = Curso()

    def list_cursos(self):
        cursos = self.curso.get_curso_all('ID_CURSO')
        print("----------------------------")
        print("ID | NOMBRE ")
        print("----------------------------")
        for curso in cursos:
            print(curso)

    def list_curso(self, id):
        curso_one = self.curso.get_curso({'ID_CURSO': id})
        return curso_one

    def list_curso_columns(self, data):
        cursos = self.curso.get_cursos_columns(data)
        return cursos

    def insert_curso(self, data):
        self.curso.insert_curso(data)
        print(f'\n ====> Se creo con exito el Curso {data}<====\n ')
        return True

    def update_curso(self, id_object, data):
        self.curso.update_curso(id_object, data)
        print(f'\n ====> Se actualizo con exito el Curso con los datos :  {data}<====\n ')
        return True

    def delete_curso(self, id_object):
        self.curso.delete_curso(id_object)
        print(f'\n ====> Se elimino con exito el Curso de {id_object}<====\n ')
        return True

    



