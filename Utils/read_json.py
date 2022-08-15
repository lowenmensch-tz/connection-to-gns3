import json
import os

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15

def get_data(path, filename): 
    
    import_file = open( 
        os.path.join(path, filename), 
        "r"
        )
    data = json.load(import_file)
    
    return data