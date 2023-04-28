
class MyException(Exception):
    """General exception class"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class ExceptionConnectToDB(MyException):
    """Exception. Сhecking connect to database """
    description = "Error connecting to the database"

class ExceptionReqDB(MyException):
    """Exception. Database request error """
    description = "Database request error"
