#which python3

from ExportDataSQL.run import ExportDataSQL
from FormatData.run import bgp, devices, ports

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15



if __name__ == "__main__":
    
    #Data
    tbl_devices = devices()
    tbl_ports = ports()
    tbl_bgp, tbl_bgp_neighbors, tbl_bgp_network = bgp()

    #Inserts
    export = ExportDataSQL()
    export.insert_data_in_tbldevice(tbl_devices)
    export.insert_data_in_tblports(tbl_ports)
    export.insert_data_in_tblbgp(tbl_bgp)
    export.insert_data_in_tblbgp_neighbors(tbl_bgp_neighbors)
    export.insert_data_in_tblbgp_network(tbl_bgp_network)
