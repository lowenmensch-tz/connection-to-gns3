#which python3

from ExportDataSQL.run import ExportDataSQL
from LogBGP.run import run
from ExtractData.run import run
from FormatData.run import bgp, devices, ports
from Engine.config_connection import ConfigConnection
from ExtractData.get_data_gns3_by_command import GetDataGns3ByCommand
from ExtractData.get_data_gns3_by_ip import GetDataGns3ByIP

from Engine.config_connection import ConfigConnection

# @author=kenneth.cruz@unah.hn
# @version=0.1.3
# @date=2022/08/15

from Utils.get_dir_path import get_dir_path
import os

def extract_data():
        
    #Configuración de todos los routers
    config = ConfigConnection(
                "config_router"
            ).get_all_data_config()

    router = GetDataGns3ByIP(config)
    GetDataGns3ByCommand(router).show_ip_int_brief()
    GetDataGns3ByCommand(router).show_version()
    GetDataGns3ByCommand(router).show_hardware()
    GetDataGns3ByCommand(router).show_bgp_summary()
    GetDataGns3ByCommand(router).show_running_section_bgp()
    GetDataGns3ByCommand(router).show_ip_bgp()


def populate_db():
    
    #Data
    data_devices = devices()
    data_ports = ports()
    data_bgp, data_bgp_neighbors, data_bgp_network = bgp()

    #Inserts
    export = ExportDataSQL()
    export.insert_data_in_tbldevice(data_devices)
    export.insert_data_in_tblports(data_ports)
    export.insert_data_in_tblbgp(data_bgp)
    export.insert_data_in_tblbgp_neighbors(data_bgp_neighbors)
    export.insert_data_in_tblbgp_network(data_bgp_network)


def log_bgp():
    run()
    

if __name__ == "__main__":
    #populate_db()
    #log_bgp()
    extract_data()
