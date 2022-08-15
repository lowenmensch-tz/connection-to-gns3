import re
import os
import json

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/14


class ProcessPortData: 

    def __init__(self, json_filename=None):
        """
            @brief: Constructor de la clase
            @param: json_filename: nombre del JSON que se va a importar
        """
        self.path = os.path.realpath(__file__)
        self.filename = os.path.basename(__file__)
        self.data = None
        self.json_filename = json_filename


    def format_int_brief(self):
        """
            @brief: Formatea la data obtenida del router por medio del comando 'show version'
            sustrae la siguiente información:
                - int
                - ipaddr
                - status (proto)
        """

        self.json_filename = "show_ip_int_brief"
        self.data = self.import_data_to_JSON()
        
        new_data = self.data[0]
        keys_to_save = ["status"]

        dict_temporal_data = {}
        current_data = []

        for keys, values in new_data.items():
            for i in values:
                for key, value in i.items():
                    if key not in keys_to_save:

                        if key == "proto": 
                            if value == "up":
                                dict_temporal_data[key] = int(1)
                            else: 
                                dict_temporal_data[key] = int(0)
                            dict_temporal_data["bit_state"] = dict_temporal_data.pop(key)
                        
                        elif key == "ipaddr":
                            
                            if value == "unassigned": 
                                dict_temporal_data[key] = None
                            else: 
                                dict_temporal_data[key] = value
                            
                            dict_temporal_data["tex_assigned_ipv4"] = dict_temporal_data.pop(key)
                        
                        elif key == "intf":
                            dict_temporal_data[key] = value
                            dict_temporal_data["tex_name"] = dict_temporal_data.pop(key)

                current_data.append(dict_temporal_data)
                dict_temporal_data = {}
            new_data[keys] = current_data
            current_data = []
        
        return new_data
        
            
    def import_data_to_JSON(self): 
        
        filename = "Data/{}.json".format(self.json_filename)
        path = self.path.replace(self.filename, filename).replace("FormatData", "ExtractData")

        import_file = open(path, "r")
        data = json.load(import_file)
        
        return data

"""
if __name__ == "__main__":
    print(
        ProcessPortData().format_int_brief()
    )
"""