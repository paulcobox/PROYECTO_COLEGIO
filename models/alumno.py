from connection.conn import Connection

class Alumno:
    def __init__(self):
        self.model = Connection('ALUMNO')

    def get_alumno_all(self, order):
        return self.model.get_all(order)

    def get_alumno(self, id_object):
        return self.model.get_by_id(id_object)

    def get_alumnos_columns(self, id_object):
        return self.model.get_columns(id_object)

    def insert_alumno(self, data):
        return self.model.insert(data)

    def update_alumno(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_alumno(self, id_object):
        return self.model.delete(id_object)