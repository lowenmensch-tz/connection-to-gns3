
from Engine.engine_connection import Engine
from mysql.connector import errorcode
import mysql.connector
import re

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/14


class MySQLEngine: 

    def __init__(self):
        self.cnx, self.link = Engine().connection()

    
    def insert(self, table, fields, values):
        """
            @brief: Inserta los datos en la base de datos
        """
        try: 
            
            query = "INSERT INTO {0} ({1}) VALUES ({2});".format( 
                    table, 
                    ", ".join(fields), 
                    self.format_key(values) 
                )
            #print(query)
            self.link.execute(query, values)
            self.cnx.commit()


        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None

    
    def format_key(self, values):
        
        new_data = ["%s" for value in values]
        join_data = ", ".join(new_data)
        return join_data


    # Función que encapsula la operación de select 
    # cursor.execute(query, data)
    def select(self, query, data=()): 

        try:         
            # Se comprueba si se recibió un parámetro data
            if len(data):
                self.link.execute(query, data)
            else: 
                self.link.execute(query)

            # Retorna los elementos que se obtuvieron al hacer la operación de select
            return self.link.fetchall()

        except mysql.connector.Error as e:
            print(e)