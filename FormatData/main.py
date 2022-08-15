from FormatData.process_bgp_data import ProcessBGPData
from FormatData.process_device_data import ProcessDeviceData
from FormatData.process_ports_data import ProcessPortData

# @author=kenneth.cruz@unah.hn
# @version=0.1.0
# @date=2022/08/12

def bgp():
    """
        @brief: Función que obtiene los datos formateados del bgp para cada router
    """
    data_bgp_summary = ProcessBGPData(
                json_filename="show_bgp_summary"
            ).format_bgp_command(
                    regex=r'^BGP router identifier (\d{1,2}\.){3}\d{1,2}, local AS number \d{5}$'
                )

    bgp = ProcessBGPData().format_bgp_summary(data_bgp_summary)

    bgp_neighbors = ProcessBGPData(
                json_filename="show_running-config__section_bgp"
            ).format_bgp_command(
                    regex=r'^neighbor (\d{1,2}\.){3}\d{1,2} remote-as \d{5}$'
                )

    bgp_network = ProcessBGPData(
                json_filename="show_ip_bgp"
            ).format_ip_bgp()

    return (
        bgp,
        bgp_neighbors,
        bgp_network
    )


def devices():
    """
        @brief: Función que obtiene los datos formateados del devices para cada router
    """

    device_data = ProcessDeviceData().join_format_data()
    return device_data


def ports():
    """
        @brief: Función que obtiene los datos formateados del ports para cada router
    """
    port_data = ProcessPortData().format_int_brief()
    return port_data

"""
if __name__ == '__main__':
    
    tbl_devices = devices()
    tbl_ports = ports()
    tbl_bgp, tbl_bgp_neighbors, tbl_bgp_network = bgp()
"""