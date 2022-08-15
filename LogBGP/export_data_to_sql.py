
from ExportDataSQL.mysql_engine import MySQLEngine


# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/15


def insert_data_in_tbllog_bgp_peer_connectivity(tbl_bgp_log):
    """
        @brief: Inserta los datos a la tabla bgpnetwork
        @param: tbl_bgp_network - data a insertar
    """
    
    db = MySQLEngine()

    for keys, values in tbl_bgp_log.items():
        
        if len(values) > 1:
            id = db.select("SELECT bgp.id  FROM device INNER JOIN bgp ON device.id = bgp.id_device_fk WHERE device.tex_username = %s", (keys,))
            for value in values:
                if len(value) > 1:
                    value['id_bgp_fk'] = id[0][0]
                    db.insert("logbgppeerconnectivity", list(value.keys()), list(value.values()))
                    print(value)
    print("Done")