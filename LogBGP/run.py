from LogBGP.export_data_gns3 import ExportDataGNS3
from LogBGP.format_data_gns3 import format_bgp_command
from LogBGP.export_data_to_sql import insert_data_in_tbllog_bgp_peer_connectivity
from Engine.config_connection import ConfigConnection
from ExtractData.get_data_all_devices_by_ip import GetDataAllDevicesByIP

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15
        


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
    gns3 = (ExportDataGNS3(router)).show_bgp_summary()
    tbl_bgp_log = format_bgp_command()
    insert_data_in_tbllog_bgp_peer_connectivity(tbl_bgp_log)



"""
if __name__ == '__main__':
    run()
"""

"""
['Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd', 

'15.15.15.5      4        65200      34      36       14    0    0 00:24:21       10', 
'15.15.15.10     4        65400      35      36       14    0    0 00:24:27       10']
"""