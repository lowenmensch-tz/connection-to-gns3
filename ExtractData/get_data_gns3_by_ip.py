import re
from netmiko import ConnectHandler

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12


class GetDataGns3ByIP:
    
    def __init__(self, config):
        """
            @param: config: Configuracion de la conexión hacia los routers
            @param: config: Información de los routers (device_type, host, username, password)
        """        
        self.config = config
        
    
    def connect_devices(self, command):
        """
            @brief: Envía la configuración de todos los dispositivos a la vez
            @param: command: Comando a ejecutar
        """
        data = [{}]
        
        for value in self.config.values(): 

            data[0][value['username']] = self.connect_device(command, value)

        return data


    def connect_device(self, command, config):
        """
            @brief: Funcion que permite conectarse a un dispositivo y ejecutar un comando
            @param: config: Configuracion de la conexión
            @param: command: Comando a ejecutar
        """
        with ConnectHandler(**config) as net_connect:
            output = net_connect.send_command(
                                command, 
                                use_textfsm=True, 
                                read_timeout=30
                            )
        
        return output
