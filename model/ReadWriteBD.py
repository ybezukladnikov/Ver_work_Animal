import pymysql

from config import host, user, password, db_name
from model.Exception import ExceptionReqDB, ExceptionConnectToDB


class ReadWriteBD:
    def read_write_bd(self, command, flag):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    cursor.execute(command)
                    if flag == 'r':
                        rows = cursor.fetchall()
                        return rows
                    elif flag == 'w':
                        connection.commit()


            except Exception:
                raise ExceptionReqDB()

            finally:
                connection.close()

        except ExceptionReqDB:
            print(ExceptionReqDB.description)
            exit()
        except Exception:
            raise ExceptionConnectToDB("Error connecting to the database")

    # def write_bd(self, command):
    #     try:
    #         connection = pymysql.connect(
    #             host=host,
    #             port=3306,
    #             user=user,
    #             password=password,
    #             database=db_name,
    #             cursorclass=pymysql.cursors.DictCursor
    #         )
    #
    #         try:
    #             with connection.cursor() as cursor:
    #                 cursor.execute(command)
    #                 connection.commit()
    #         except Exception:
    #             raise ExceptionReqDB()
    #
    #         finally:
    #             connection.close()
    #
    #     except ExceptionReqDB:
    #         print(ExceptionReqDB.description)
    #         exit()
    #     except Exception:
    #         raise ExceptionConnectToDB("Error connecting to the database")
    #






