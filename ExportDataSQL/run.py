#which python3

from ExportDataSQL.mysql_engine import MySQLEngine

# @author=kenneth.cruz@unah.hn
# @version=0.1.2
# @date=2022/08/12


class ExportDataSQL:

    def __init__(self): 
        self.db = MySQLEngine()

    def insert_data_in_tbldevice(self, tbl_devices): 

        for key, value in tbl_devices.items():
            self.db.insert("device", list(value.keys()), list(value.values()))

        print("Done")


    def insert_data_in_tblports(self, tbl_ports): 

        for keys, values in tbl_ports.items():
            id = self.db.select("SELECT id FROM device WHERE tex_username = %s", (keys,))
            for value in values:
                value['id_device_fk'] = id[0][0]
                self.db.insert("ports", list(value.keys()), list(value.values()))

        print("Done")


    def insert_data_in_tblbgp(self, tbl_bgp): 
        """
            @brief: Inserta los datos a la tabla bgp
            @param: tbl_bgp - data a insertar
        """

        for keys, values in tbl_bgp.items():
            id = self.db.select("SELECT id FROM device WHERE tex_username = %s", (keys,))

            if len(values) > 0:
                for value in values:
                    value['id_device_fk'] = id[0][0]
                    self.db.insert("bgp", list(value.keys()), list(value.values()))

        print("Done")


    def insert_data_in_tblbgp_network(self, tbl_bgp_network):
        """
            @brief: Inserta los datos a la tabla bgpnetwork
            @param: tbl_bgp_network - data a insertar
        """
        
        for keys, values in tbl_bgp_network.items():
            
            if len(values) > 1:
                id = self.db.select("SELECT bgp.id  FROM device INNER JOIN bgp ON device.id = bgp.id_device_fk WHERE device.tex_username = %s", (keys,))
                for value in values:
                    if len(value) > 1:
                        value['id_bgp_fk'] = id[0][0]
                        self.db.insert("bgpnetwork", list(value.keys()), list(value.values()))
        print("Done")


    def insert_data_in_tblbgp_neighbors(self, tbl_bgp_neighbors): 
        """
            @brief: Inserta los datos a la tabla bgpneighbors
            @param: tbl_bgp_neighbors - data a insertar
        """

        current_data = {}

        for keys, values in tbl_bgp_neighbors.items():
            bgp_id = self.db.select("SELECT bgp.id  FROM device INNER JOIN bgp ON device.id = bgp.id_device_fk WHERE device.tex_username = %s", (keys,))
            if len(values) > 0:
                for value in values:
                    current_data['id_bgp_fk'] = bgp_id[0][0]
                    current_data['tex_neighbor'] = (value.replace("neighbor", "")).strip()
                    self.db.insert("bgpneighbor", list(current_data.keys()), list(current_data.values()))
        print("Done")