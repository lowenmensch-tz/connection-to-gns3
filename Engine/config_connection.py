# -*- coding: utf-8 -*-

# @author: kenneth.cruz@unah.hn
# @version: 0.1.0
# @date: 2022/08/12


import configparser
import os
import re

class ConfigConnection: 

    def __init__(self, filename): 
        try: 
            #Ruta del archivo de configuración
            self.path =  re.sub(r"(config_connection.py)", "Config/{0}.ini".format(filename), os.path.realpath(__file__) )
            #Instancia del objeto configparser
            self.parser = configparser.ConfigParser()
            #Lectura el archivo config.ini
            self.parser.read(self.path)

        except os.error as e:
            print(e)
            pass
        
    #Toma los valores del archivo de configuración; retorna un diccionario
    def getConfig(self): 
        
        #Sección por defecto dentro del archivo de configuración (config.ini)
        config = self.parser["DEFAULT"]
        
        #Configuración de la conexión a la base de datos
        config = dict(zip(config.keys(), config.values()))

        return config