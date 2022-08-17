import json
import os
import re
from datetime import datetime
from Utils.get_dir_path import get_dir_path
from Utils.export_data_to_json import export_data_to_JSON

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12

class GetDataGns3ByCommand:

    def __init__(self, router) -> None:
        """
            @brief: Constructor de la clase
            @param: router: Objeto de la clase GetDataGns3ByIP
        """
        self.command = None
        self.router = router

        self.path = os.path.realpath(__file__)
        self.dir_path = get_dir_path(self.path)

    
    def show_ip_int_brief(self):
        
        self.command = "show ip int brief"
        self.save_data()


    def show_version(self):
        
        self.command = "show version"
        self.save_data()


    def show_hardware(self):
        
        self.command = "show hardware"
        self.save_data()


    def show_bgp_summary(self):
        
        self.command = "show bgp summary"
        self.save_data()

    
    def show_running_section_bgp(self):
        
        self.command = "show running-config | section bgp"
        self.save_data()

    
    def show_ip_bgp(self):
            
        self.command = "show ip bgp"
        self.save_data()


    def save_data(self): 
        
        data = self.router.connect_devices(self.command)
        filename = self.filename()
        export_data_to_JSON(
                    path=os.path.join(
                        self.dir_path, 
                        "Data"), 
                    data=data, 
                    filename=filename
                )

        print("Done! {}.json created".format(filename))


    def filename(self): 
        """
            @brief: Asigna un nombre a partir de la fecha actual y el comando ejecutado
        """
        f = lambda command: re.sub(r"[\s|-]+", "_", command)

        timestamp = datetime.now()
        filename = timestamp.strftime("{}_%Y_%m_%d_%H%M%S".format(
                f(self.command))
            )
        return filename