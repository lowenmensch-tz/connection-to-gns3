# -*- coding: utf-8 -*-

# @author: kenneth.cruz@unah.hn
# @version: 0.1.2
# @date: 2022/08/12


import configparser
import os

class ConfigConnection: 

    def __init__(self, filename, ini_path=None): 
        try: 
            
            if ini_path is None: 
                self.path = os.path.realpath(__file__)
                self.dir_path = self.path.split("\\")[:-1]
                self.ini_path = os.path.join(
                    "\\".join(self.dir_path), 
                    "Config", 
                    "{0}.ini".format(filename)
                )
            else: 
                self.ini_path = ini_path

            self.parser = configparser.ConfigParser()
            self.parser.read(self.ini_path)
            

        except os.error as e:
            print(e)
            pass
        
    
    def getConfig(self, section): 
        """
            @brief: Retorna todas las opciones de una sección del archivo de configuración.
        """

        config = self.parser[section]
        config = dict(zip(config.keys(), config.values()))

        return config

    
    def get_section(self): 
        """
            @brief: Retorna todas las secciones del archivo de configuración.
        """
        output = self.parser.sections()
        return output


    def get_all_data_config(self): 
        """
            @brief: Retorna todos los datos del archivo de configuración.
        """
        
        sections = self.get_section()
        output = {}

        for section in sections:
            output[section] = self.getConfig(section)

        return output