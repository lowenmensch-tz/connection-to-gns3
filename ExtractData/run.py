from Engine.config_connection import ConfigConnection
from ExtractData.get_data_gns3_by_command import GetDataGns3ByCommand
from ExtractData.get_data_gns3_by_ip import GetDataGns3ByIP

# @author=kenneth.cruz@unah.hn
# @version=0.1.1
# @date=2022/08/12
        

def run():
    
    #Configuració de todos los routers
    config = ConfigConnection(
                "config_router"
            ).get_all_data_config()

    router = GetDataGns3ByIP(config)
    #GetDataGns3ByCommand(router).show_ip_int_brief()
    #GetDataGns3ByCommand(router).show_version()
    #GetDataGns3ByCommand(router).show_hardware()
    #GetDataGns3ByCommand(router).show_bgp_summary()
    #GetDataGns3ByCommand(router).show_running_section_bgp()
    #GetDataGns3ByCommand(router).show_ip_bgp()

    print("Done")