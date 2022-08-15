# Librerias usadas
# python -m pip install pymongo
# python -m pip install dnspython
from datetime import datetime

#Funcion para acceder a la base de datos
def get_database():
    from pymongo import MongoClient

    # Direccion de la base de datos de MongoDB 
    CONNECTION_STRING = "mongodb+srv://admin:redes_2@cluster0.cjtqirz.mongodb.net/test"

    # Crear la conexion usando el mondoDB Atlas
    client = MongoClient(CONNECTION_STRING)

    #Crear la base de datos
    return client['networks']

#Funcion para insertar un nuevo dispositivo

def insert_item(item):
    db = get_database()
    collection = db['device']
    if collection.find_one({'id': item['id']}):
        print("Item ya existe")
        return False
    else:
        collection.insert_one(item)
        print("Item insertado")
        return True 
        
def insert_log(log):
    db = get_database()
    collection = db['log']
    if collection.find_one({'id': log['id']}):
        print("log ya existe")
        return False
    else:
        collection.insert_one(log)
        print("log insertado")
        return True
        
#Funcion para actualizar un dispositivo
def update_by_id(id, item):
    db = get_database()
    collection = db['device']
    collection.update_one({'_id': id}, {'$set': item})
    print("Item actualizado")
    return True

def update_by_id_log(id, item):
    db = get_database()
    collection = db['log']
    collection.update_one({'_id': id}, {'$set': item})
    print("Item actualizado")
    return True

#Funcion para eliminar un dispositivo

def delete_by_id(id):
    db = get_database()
    collection = db['device']
    collection.delete_one({'_id': id})
    print("Item eliminado")
    return True

#obtener un dispositivo
def get_by_id(id):
    db = get_database()
    collection = db['device']
    return collection.find_one({'id': id})

def get_by_id_log(id):
    db = get_database()
    collection = db['log']
    return collection.find_one({'id': id})

# Esto se agrega para que get_database sea una funcion sea reutilizable
if __name__ == "__main__":    
    
    # ir a la base de datos
    dbname = get_database()
    
#Crear la coleccion
collection_name = dbname["device"]


item_1 = {
    "id" : "1",
    "description": "Dispositivo 1",
    "name": "Dispositivo 1",
    "version_os": "Windows 10",
    "hardware_address": "00:00:00:00:00:00",
    "username:": "admin",
    "privileges_exec_mode_password": "admin",
    "user_exec_mode_password": "admin",
    "date": datetime.now(),
    "ports": {
        "serial": "COM1",
        "name": "COM1",
        "assigned_ipv4": "0.0.0.0",
        "bit": "0",
        "date": datetime.now()
    },
    "BGP" :{
        "serial": "COM1",
        "description": "Dispositivo 1",
        "AS": "AS1",
        "router_id": "1023",
        "BGP_Network": {
            "id": "1",
            "network": ""
        },
        "BGP_Neighbor": {
            "id_bg": "1",
            "neighbor": "",
        }      
    }
}

#log_BGP_peer_conectivity

log ={
        "id": "1",
        "router_id": "1023",
        "AS": "AS1",
        "datagram_rcvd": "",
        "datagram_sent": "",
        "date": datetime.now()
    }

insert_item(item_1)
insert_log(log)

d = get_by_id("1")

#Device
description = d["description"]
name = d["name"]
version_os  = d["version_os"]
hardware_address = d["hardware_address"]
username = d["username"]
privilege_exec_mode_password = d["privileges_exec_mode_password"]
user_exec_mode_password = d["user_exec_mode_password"]
date = d["date"]
serial_port = d["ports"]["serial"]
name_port = d["ports"]["name"]
assigned_ipv4 = d["ports"]["assigned_ipv4"]
bit_port = d["ports"]["bit"]
date_port = d["ports"]["date"]
serial_bgp = d["BGP"]["serial"]
description_bgp = d["BGP"]["description"]
AS_bgp = d["BGP"]["AS"]
router_id_bgp = d["BGP"]["router_id"]
id_bgp_network = d["BGP"]["BGP_Network"]["id"]
bgp_network = d["BGP"]["BGP_Network"]["network"]
id_bgp_neighbor = d["BGP"]["BGP_Neighbor"]["id_bg"]
bgp_neigbor = d["BGP"]["BGP_Neighbor"]["neighbor"]

#log_BGP_peer_conectivity

log_BGP = get_by_id_log("1")

log_id_bgp = log_BGP["id"]
log_router_id = log_BGP["router_id"]
log_as = log_BGP["AS"]
log_rcvd = log_BGP["datagram_rcvd"]
log_sent = log_BGP["datagram_sent"]
log_date = log_BGP["date"]



