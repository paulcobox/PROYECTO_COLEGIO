from connection.conn import Connection

class Profesor:
    def __init__(self):
        self.model = Connection('PROFESOR')

    def get_profesor_all(self, order):
        return self.model.get_all(order)

    def get_profesor(self, id_object):
        return self.model.get_by_id(id_object)

    def get_profesores_columns(self, id_object):
        return self.model.get_columns(id_object)

    def insert_profesor(self, data):
        return self.model.insert(data)

    def update_profesor(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_profesor(self, id_object):
        return self.model.delete(id_object)