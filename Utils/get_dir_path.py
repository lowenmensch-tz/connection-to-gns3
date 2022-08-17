import os

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/17

def get_dir_path(path):
    
    separator = None

    #windows
    if "\\" in path:
        separator = "\\"
    #Linux
    else: 
        separator = "/"

    dir_path = separator.join(path.split(separator)[:-1])

    return dir_path