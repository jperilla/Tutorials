from abc import ABC, abstractmethod


class DatabaseBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get(self):
        pass


class MySqlDatabase(DatabaseBase):
    def __init__(self):
        super().__init__()

    def connect(self):
        # TODO: implementation for a MySQL database connection
        print("Successfully connected to MySQL database!")

    def get(self):
        return "success"  # Query the database here
