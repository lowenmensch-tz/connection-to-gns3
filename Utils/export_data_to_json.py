import json
import os

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15

def export_data_to_JSON(path, data, filename): 
    
    with open(os.path.join(
                path, 
                "{}.json".format(filename.strip())
                ), 
            "w") as outfile:

        json.dump(data, outfile)
