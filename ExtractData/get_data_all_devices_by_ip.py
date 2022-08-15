import re
from netmiko import ConnectHandler

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12


class GetDataAllDevicesByIP:
    
    def __init__(self, config, hosts):
        """
            @param: config: Configuracion de la conexión hacia los routers
            @param: hosts: ip's de los routers
        """        
        self.config = config
        self.hosts = hosts
    
    def update_username(self, username, index):
        """
            @brief: Funcion que permite cambiar el nombre de usuario de los routers
            @param: username: Nombre de usuario
            @param: index: Indice del router
        """
        username = re.sub(r"(\d+)", str(index+1), username)
        return username


    def connect_devices(self, command):

        data = [{}]
        
        for i in range(len(self.hosts)): 

            self.config['host'] = self.hosts[i]
            self.config['username'] = self.update_username(self.config['username'], i)

            data[0][self.config['username']] = self.connect_device(command)

        return data


    def connect_device(self, command):
        """
            @brief: Funcion que permite conectarse a un dispositivo y ejecutar un comando
            @param: config: Configuracion de la conexión
            @param: command: Comando a ejecutar
        """
        with ConnectHandler(**self.config) as net_connect:
            # Use TextFSM to retrieve structured data
            output = net_connect.send_command(
                                command, 
                                use_textfsm=True, 
                                read_timeout=30
                            )
        
        return output
