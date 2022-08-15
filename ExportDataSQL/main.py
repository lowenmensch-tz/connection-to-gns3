from ExportDataSQL.mysql_engine import MySQLEngine
from FormatData.main import bgp, devices, ports

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12



def insert_data_in_tbldevice(tbl_devices): 

    for key, value in tbl_devices.items():
        db.insert("device", list(value.keys()), list(value.values()))

    print("Done")


def insert_data_in_tblports(tbl_ports): 

    for keys, values in tbl_ports.items():
        id = db.select("SELECT id FROM device WHERE tex_username = %s", (keys,))
        for value in values:
            value['id_device_fk'] = id[0][0]
            db.insert("ports", list(value.keys()), list(value.values()))

    print("Done")


if __name__ == "__main__":
    
    db = MySQLEngine()
    tbl_devices = devices()
    tbl_ports = ports()
    tbl_bgp, tbl_bgp_neighbors, tbl_bgp_network = bgp()


    print(tbl_bgp)