

class AlunoRepository():
    def __init__(self, connection):
        self.connection = connection

    def create(self):
        self.connection.create()

    def delete_one(self):
        pass