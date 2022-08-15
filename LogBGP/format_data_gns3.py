from Utils.read_json import get_data
import os
import re

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15


#os.listdir

path = os.path.realpath(__file__)
dir_path = path.split("\\")[:-1]
json_path = os.path.join(
                "\\".join(dir_path), 
                "Data"
            )

list_filename = os.listdir(json_path)

json_data = get_data(
            path=json_path,
            filename=list_filename[-1]
        )


def format_bgp_command():
    
    new_data = []
    current_dict_data = {}
    data = {}

    for keys, values in json_data[0].items():
        values = values.split("\n")[12:]

        for value in values:
            value = (re.sub(r"\s+", "-",  value)).split("-")
            current_dict_data['tex_neighbor'] = value[0]
            current_dict_data['tex_as'] = value[2]
            current_dict_data['tex_datagram_rcvd'] = value[3]
            current_dict_data['tex_datagram_sent'] = value[4]
            current_dict_data['tim_time_up'] = value[8]

            new_data.append(current_dict_data)
            current_dict_data = {}

        data[keys] = new_data
        new_data = []

    return data