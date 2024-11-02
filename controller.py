from database import Database


class Controller:
    def __init__(self):
        self.db = Database()
        self.db.conecta()
        self.db.create_tables()

    def close_db(self):
        self.db.close_connection()
