import os
from datetime import datetime  
from Utils.export_data_to_json import export_data_to_JSON

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15
        

class ExportDataGNS3: 

    def __init__(self, router):
        self.router = router 
        self.command = None
        

    def show_bgp_summary(self):
        
        self.command = "show bgp summary"
        self.save_data()


    def save_data(self): 
        
        timestamp = datetime.now()
        filename = timestamp.strftime("bgp_summary_%Y_%m_%d_%H%M%S")
        data = self.router.connect_devices(self.command)
        
        path = os.path.realpath(__file__)
        path = os.path.join(
                "\\".join(path.split("\\")[:-1]), 
                "Data"
            )
        export_data_to_JSON(
                        filename=filename, 
                        data=data, 
                        path=path
                )
        print("Done! \n{}.json is created".format(filename))