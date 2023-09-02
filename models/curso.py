from connection.conn import Connection

class Curso:
    def __init__(self):
        self.model = Connection('CURSO')

    def get_curso_all(self, order):
        return self.model.get_all(order)

    def get_curso(self, id_object):
        return self.model.get_by_id(id_object)

    def get_cursos_columns(self, id_object):
        return self.model.get_columns(id_object)

    def insert_curso(self, data):
        return self.model.insert(data)

    def update_curso(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_curso(self, id_object):
        return self.model.delete(id_object)