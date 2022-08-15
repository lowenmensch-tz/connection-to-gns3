from ntpath import join
import re
import os
import json
from copy import deepcopy
from Engine.config_connection import ConfigConnection


# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/14


class ProcessDeviceData: 

    def __init__(self, json_filename=None):
        """
            @brief: Constructor de la clase
            @param: json_filename: nombre del JSON que se va a importar
        """
        self.path = os.path.realpath(__file__)
        self.filename = os.path.basename(__file__)
        self.data = None
        self.json_filename = json_filename

    
    def format_hardware(self):
        """
            @brief: Formatea la data obtenida del router por medio del comando 'show hardware'
            sustrae la siguiente información:
            - Modelo y fabricante del router
            - versión del OS 
        """
        self.json_filename = "show_hardware"
        self.data = self.import_data_to_JSON()
        new_data = self.data[0]
        
        dict_temporal_data = {}

        for key, value in new_data.items():
            
            all_data = value.split("\n")
            temporal_data = all_data[0].split(",")

            dict_temporal_data['tex_description'] = (temporal_data[0] + " " + temporal_data[1]).strip()
            dict_temporal_data['tex_version_os'] = (temporal_data[2].replace("Version", "")).strip()
            dict_temporal_data['tex_cpu_info'] = ",".join([ x.strip() for x in all_data if "memory" in x ])
            dict_temporal_data['tex_username'] = key
            dict_temporal_data['tex_privileged_exec_mode_password'] = ConfigConnection("config_router").getConfig()['password']


            new_data[key] = [ dict_temporal_data ]
            dict_temporal_data = {}


        return new_data


    def format_version(self):
        """
            @brief: Formatea la data obtenida del router por medio del comando 'show version'
            sustrae la siguiente información:
                - uptime
                - hostname
                - hardware
                - serial
                - config_register
                - mac
        """
        self.json_filename = "show_version"
        self.data = self.import_data_to_JSON()
        
        new_data = self.data[0]
        keys_to_save = ["hostname", "serial"]
        
        dict_temporal_data = {}

        for keys, values in new_data.items():
            
            for key, value in values[0].items(): 
                if key in keys_to_save:
                    if key == "hostname":
                        dict_temporal_data[key] = value
                        dict_temporal_data["tex_hostname"] = dict_temporal_data.pop(key)
                    elif key == "serial":
                        dict_temporal_data[key] = value[0]
                        dict_temporal_data["tex_serial_hardware"] = dict_temporal_data.pop(key)
            
            new_data[keys] = [ dict_temporal_data ]
            dict_temporal_data = {}

        return new_data

    
    def import_data_to_JSON(self): 
        
        filename = "Data/{}.json".format(self.json_filename)
        path = self.path.replace(self.filename, filename).replace("FormatData", "ExtractData")

        import_file = open(path, "r")
        data = json.load(import_file)
        
        return data

    
    def join_format_data(self):
        """
            @brief: une toda la data obtenida del router en un solo diccionario
            - description
            - version_os
            - name (hostname)
            - hardware
            - serial
            - username
            - privileged_exec_mode_password
            - user_exec_mode_password
        """
        data_hardware = self.format_hardware()
        data_version = self.format_version()
        
        new_data = self.dict_of_dicts_merge(data_hardware, data_version)
        return new_data


    def dict_of_dicts_merge(self, x, y):
        z = {}
        overlapping_keys = x.keys() & y.keys()
        for key in overlapping_keys:
            z[key] = self.dict_of_dicts_merge(x[key][0], y[key][0])
        for key in x.keys() - overlapping_keys:
            z[key] = deepcopy(x[key])
        for key in y.keys() - overlapping_keys:
            z[key] = deepcopy(y[key])
        return z


"""
if __name__ == "__main__": 

    print(
        ProcessDeviceData().join_format_data()
        #ProcessDeviceData().format_hardware()
        #ProcessDeviceData().format_version()
    )
"""