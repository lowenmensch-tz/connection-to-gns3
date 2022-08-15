from Engine.config_connection import ConfigConnection
from ExtractData.get_data_from_devices import GetDataFromDevices
from ExtractData.get_data_all_devices_by_ip import GetDataAllDevicesByIP

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12
        

def run():
    
    config = ConfigConnection("config_router").getConfig()

    # Ip de los routers
    hosts = [
        '15.15.15.1', 
        '15.15.15.18',  
        '15.15.15.17', 
        '15.15.15.14', 
        '192.178.0.2', 
        '192.178.0.6', 
        '10.10.10.1',  
        '192.178.0.5'
    ]

    router = GetDataAllDevicesByIP(config, hosts)
    #GetDataFromDevices(router).show_ip_int_brief()
    #GetDataFromDevices(router).show_version()
    #GetDataFromDevices(router).show_hardware()
    #GetDataFromDevices(router).show_bgp_summary()
    #GetDataFromDevices(router).show_running_section_bgp()
    GetDataFromDevices(router).show_ip_bgp()


if __name__ == '__main__':
    run()