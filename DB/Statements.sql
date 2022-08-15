
USE NetworkAutomation;

-- --------------------------------------------
-- Información general de todos los dispositivos
-- --------------------------------------------
SELECT 
    Device.tex_hostname Hostname, 
    Device.tex_version_os OS, 
    REGEXP_SUBSTR(Device.tex_cpu_info, '[0-9]+k/[0-9]+k') Memory,
    Device.tex_username Username, 
    Device.tex_privileged_exec_mode_password Password, 
    ActivePorts.NumberActivePorts 'Number Active Ports'
FROM 
    Device
INNER JOIN (
    SELECT 
        Ports.id_device_fk id,
        COUNT(*) AS NumberActivePorts
    FROM 
        Ports
    WHERE
        Ports.bit_state = 1
    GROUP BY
        Ports.id_device_fk
) AS ActivePorts 
    ON ActivePorts.id = Device.id
ORDER BY 
    Device.tex_hostname;


-- --------------------------------------------
-- Puertos activos para un Router según el HOSTNAME
-- --------------------------------------------
SELECT 
    Ports.tex_name Interface, 
    Ports.tex_assigned_ipv4 IPV4
FROM 
    Ports
INNER JOIN Device
    ON Ports.id_device_fk = Device.id
WHERE 
    Device.tex_hostname = 'R1'
    AND Ports.bit_state = 1;



-- --------------------------------------------
-- BGP activo en los dispositivos: 
-- --------------------------------------------
SELECT 
    Device.tex_hostname Hostname, 
    Device.tex_version_os OS, 
    Device.tex_username Username, 
    Device.tex_privileged_exec_mode_password Password, 
    ActivePorts.NumberActivePorts 'Number Active Ports',
    IF(BGP.id, 'Active', 'No Active') 'BGP', 
    BGP.tex_as 'AS', 
    BGP.tex_router_id 'router-id'
FROM 
    Device
INNER JOIN (
    SELECT 
        Ports.id_device_fk id,
        COUNT(*) AS NumberActivePorts
    FROM 
        Ports
    WHERE
        Ports.bit_state = 1
    GROUP BY
        Ports.id_device_fk
) AS ActivePorts 
    ON ActivePorts.id = Device.id
INNER JOIN BGP
    ON BGP.id_device_fk = Device.id
ORDER BY 
    Device.tex_hostname;


-- --------------------------------------------
-- 
-- --------------------------------------------
