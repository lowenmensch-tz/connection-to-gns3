import mysql.connector
from mysql.connector import errorcode
from Engine.config_connection import ConfigConnection

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12


class Engine: 

    def __init__(self):
        self.config = ConfigConnection("config").getConfig()


    def mysql_connect(self):
        """
            @brief: Conecta a la base de datos
            @param: tunnel: Objeto de conexión a la base de datos
        """
        try: 
            cnx = mysql.connector.connect(**self.config)

            link = cnx.cursor()
            return (cnx, link)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None


    def connection(self):
        cnx, link = self.mysql_connect()
        return cnx, link

"""
if __name__ == "__main__":

    link.execute("SHOW TABLES")
    
    print( link.fetchall() )
    cnx.close()
"""