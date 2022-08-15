import json

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12

class GetDataFromDevices:

    def __init__(self, router) -> None:
        """
            @brief: Constructor de la clase
            @param: router: Objeto de la clase GetDataAllDevicesByIP
        """
        self.command = None
        self.router = router

    
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
        print(data)
        self.export_data_to_JSON(data)


    def export_data_to_JSON(self, data): 
        
        with open("./Data/{}.json".format(self.command.replace(" ", "_").replace("|", "")), "w") as outfile:
            json.dump(data, outfile)