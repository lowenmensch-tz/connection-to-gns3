/*
	author @kenne
    version 0.1.2
    date 8/9/2022
*/

DROP DATABASE IF EXISTS NetworkAutomation;

CREATE DATABASE IF NOT EXISTS NetworkAutomation;

USE NetworkAutomation;

CREATE TABLE Device(
	id SERIAL PRIMARY KEY,
    tex_description VARCHAR(100) NOT NULL COMMENT "Breve descripción del dispositivo",
	tex_hostname VARCHAR(20) NOT NULL COMMENT "Nombre deL dispositivo 'R-CORE'",
    tex_version_os VARCHAR(20) NOT NULL  COMMENT "Versión del OS",
    tex_cpu_info VARCHAR(100) NOT NULL COMMENT "Serie de CPU", 
    tex_serial_hardware VARCHAR(14) NOT NULL COMMENT "Serie de la placa", 
    tex_username VARCHAR(30) NOT NULL COMMENT "Nombre de usuario", 
	tex_privileged_exec_mode_password VARCHAR(50) COMMENT "Contraseña del modo EXEC privilegiado",
    tex_user_exec_mode_password VARCHAR(50) COMMENT "Contraseña del modo EXEC usuario", 
    tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "Fecha en que se registró el dispositivo"
)	COMMENT "Configuración inicial de los dispositivos, contraseña";

CREATE TABLE Ports(
	id SERIAL PRIMARY KEY, 
	id_device_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Device",
    tex_name VARCHAR(22) NOT NULL COMMENT "Nombre del puerto 'serial0/0/0'",
    tex_assigned_ipv4 VARCHAR(32) COMMENT "ipv4 y máscara asignada a la interfaz",
	bit_state BIT(1) NOT NULL DEFAULT 0 COMMENT "0 el puerto está disponible | 1  el puerto NO está disponible", 
    tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "Fecha en que se registró el dispositivo",
    
    FOREIGN KEY (id_device_fk) REFERENCES Device(id)
)COMMENT "Configuración de los puetos del dispositivo";


CREATE TABLE BGP(
	id SERIAL PRIMARY KEY, 
    id_device_fk BIGINT UNSIGNED UNIQUE NOT NULL COMMENT "Referencia hacia la entidad Device",
    tex_description VARCHAR(100) COMMENT "Descripción del protocolo sobre el dispositivo",
    tex_as VARCHAR(5) NOT NULL COMMENT "AS del BGP",
    tex_router_id VARCHAR(15) NOT NULL COMMENT "router-id",
    
    FOREIGN KEY (id_device_fk) REFERENCES Device(id)
)COMMENT "Configuración del BGP";


CREATE TABLE BGPNeighbor(
	id SERIAL PRIMARY KEY, 
    id_bgp_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad BGP",
    tex_neighbor VARCHAR(32) NOT NULL COMMENT "e.g. 10.12.1.1 remote-as 65200",
    
    FOREIGN KEY (id_bgp_fk) REFERENCES BGP(id)
)COMMENT "Configuración de los vecinos BGP";


CREATE TABLE BGPNetwork(
	id SERIAL PRIMARY KEY, 
    id_bgp_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad BGP",
    tex_network VARCHAR(32) NOT NULL COMMENT "e.g. ipv4 y máscara asignada a la interfaz",
    tex_next_hop VARCHAR(32) NOT NULL COMMENT "Siguiente salto de la red",
    tex_as_path VARCHAR(15) NOT NULL COMMENT "AS de las redes bgp",
    
    FOREIGN KEY (id_bgp_fk) REFERENCES BGP(id)
)COMMENT "Configuración de las redes conectadas BGP";


CREATE TABLE LogBGPPeerConnectivity(
	id SERIAL PRIMARY KEY,
    tex_neighbor  VARCHAR(16) NOT NULL COMMENT "ip del vecino",
    tex_router_id VARCHAR(15) NOT NULL COMMENT "ID",
    tex_as VARCHAR(15) NOT NULL COMMENT "AS del BGP",
	tex_datagram_rcvd VARCHAR(30) NOT NULL COMMENT "Paquetes recibidos",
    tex_datagram_sent VARCHAR(30) NOT NULL COMMENT "Paquetes enviados",
	tim_date TIMESTAMP DEFAULT NOW() NOT NULL COMMENT "Fecha en que se verificó el status de los vecinos"

)COMMENT "Log de conexión para los vecinos BGP";
