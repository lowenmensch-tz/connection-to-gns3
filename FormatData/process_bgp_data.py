import re
import os
import json

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/13

class ProcessBGPData: 

    def __init__(self, json_filename=None):
        """
            @brief: Constructor de la clase
            @param: json_filename: nombre del JSON que se va a importar
        """
        self.path = os.path.realpath(__file__)
        self.filename = os.path.basename(__file__)
        self.data = None
        self.json_filename = json_filename

    def clean_data(self):
        """
            @brief: Limpia la data obtenida del router cuando los values son strings y no arrays
        """
        new_data = [{}]

        for key, value in self.data[0].items():
            new_data[0][key] = []
            for line in value.split("\n"):
                new_data[0][key].append(line.strip())
        
        return new_data


    def format_bgp_command(self, regex):
        """
            @brief: Formatea la data obtenida del router
        """
        self.data = self.import_data_to_JSON()
        new_data = self.clean_data()
        new_data = new_data[0]
        regex_match = []
        
        for key, values in new_data.items(): 
            for value in values:
                if re.search(regex, value):
                    regex_match.append(value)
            
            new_data[key] = regex_match
            regex_match = []

        return new_data


    def format_bgp_summary(self, data):
        """
            @brief: Formatea la data obtenida del router
        """
        
        dict_temporal_data = {}

        for keys, values in data.items():
            if len(values) > 0:
                split_values = values[0].split(",")
                
                ipv4 = re.search(r"(\d{1,3}\.){3}\d{1,3}", split_values[0]).group(0)
                as_number = re.search(r"\d{5}", split_values[1]).group(0)

                dict_temporal_data["tex_router_id"] = ipv4
                dict_temporal_data["sml_as"] = int(as_number)

                data[keys] = [dict_temporal_data]
                dict_temporal_data = {}

        return data


    def format_ip_bgp(self):
        """
            @brief: Filtra toda la data obtenida del router a tres keys por router: 
                network
                next_hop
                as_path
        """
        keys_to_save = ["network", "next_hop", "as_path"]
        self.data = self.import_data_to_JSON()
        new_data = self.data[0]
        
        dict_temporal_data = {}
        temporal_data = []

        for keys, values in new_data.items():
            
            for value in values:
                if isinstance(value, dict):
                    for key in keys_to_save:
                        dict_temporal_data[key] = value[key]

                    temporal_data.append(dict_temporal_data)
            
            new_data[keys] = temporal_data
            temporal_data = [{}]
        
        return new_data

    
    def import_data_to_JSON(self): 
        
        filename = "Data/{}.json".format(self.json_filename)
        path = self.path.replace(self.filename, filename).replace("FormatData", "ExtractData")

        import_file = open(path, "r")
        data = json.load(import_file)
        
        return data


    """
if __name__ == '__main__':
    format_bgp_summary
    ----------------------
    regex =  r'^BGP router identifier (\d{1,2}\.){3}\d{1,2}, local AS number \d{5}$'
    json_filename = "show_bgp_summary"

    format_neighbors_details
    ----------------------
    regex =  r'^neighbor (\d{1,2}\.){3}\d{1,2} remote-as \d{5}$'
    json_filename = "show_running-config__section_bgp"
    """
