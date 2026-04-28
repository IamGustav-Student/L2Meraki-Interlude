import socket
import re
import urllib.request

def open_port(port, protocol='TCP', description='L2 Server'):
    print(f"Intentando abrir puerto {port} ({protocol}) vía UPnP...")
    SSDP_ADDR = "239.255.255.250"
    SSDP_PORT = 1900
    SSDP_MX = 2
    SSDP_ST = "urn:schemas-upnp-org:service:WANIPConnection:1"

    ssdpRequest = "M-SEARCH * HTTP/1.1\r\n" + \
                  "HOST: %s:%d\r\n" % (SSDP_ADDR, SSDP_PORT) + \
                  "MAN: \"ssdp:discover\"\r\n" + \
                  "MX: %d\r\n" % SSDP_MX + \
                  "ST: %s\r\n" % SSDP_ST + "\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    
    try:
        sock.sendto(ssdpRequest.encode(), (SSDP_ADDR, SSDP_PORT))
        data, addr = sock.recvfrom(1024)
        print(f"Router encontrado en: {addr[0]}")
        
        # Extraer location
        location = re.search(r'LOCATION: (.+)\r\n', data.decode(), re.IGNORECASE).group(1)
        
        # Obtener XML de control
        with urllib.request.urlopen(location) as response:
            xml = response.read().decode()
            
        control_url = ""
        # Buscamos el servicio WANIPConnection
        if "WANIPConnection" in xml:
            # Intentamos obtener la base URL si existe
            base_url_match = re.search(r'<URLBase>(.+?)</URLBase>', xml)
            base_url = base_url_match.group(1) if base_url_match else "/".join(location.split('/')[:3])
            
            # Buscamos el controlURL del servicio WANIPConnection
            service_xml = xml.split('WANIPConnection:1')[1]
            control_url_rel = re.search(r'<controlURL>(.+?)</controlURL>', service_xml).group(1)
            control_url = base_url + control_url_rel if control_url_rel.startswith('/') else "/".join(location.split('/')[:-1]) + "/" + control_url_rel

        if control_url:
            # Obtener IP local
            local_ip = socket.gethostbyname(socket.gethostname())
            
            soap_body = f"""<?xml version="1.0"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Body>
    <m:AddPortMapping xmlns:m="urn:schemas-upnp-org:service:WANIPConnection:1">
      <NewRemoteHost></NewRemoteHost>
      <NewExternalPort>{port}</NewExternalPort>
      <NewProtocol>{protocol}</NewProtocol>
      <NewInternalPort>{port}</NewInternalPort>
      <NewInternalClient>{local_ip}</NewInternalClient>
      <NewEnabled>1</NewEnabled>
      <NewPortMappingDescription>{description}</NewPortMappingDescription>
      <NewLeaseDuration>0</NewLeaseDuration>
    </m:AddPortMapping>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

            headers = {
                'SOAPAction': '"urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"',
                'Content-Type': 'text/xml'
            }

            req = urllib.request.Request(control_url, data=soap_body.encode(), headers=headers)
            with urllib.request.urlopen(req) as res:
                if res.status == 200:
                    print(f"¡Puerto {port} abierto con éxito!")
                else:
                    print(f"Error abriendo puerto {port}: {res.status}")
        else:
            print("No se pudo encontrar la URL de control UPnP.")

    except Exception as e:
        print(f"Error en UPnP: {e}. Asegúrate de que UPnP esté habilitado en tu router.")

if __name__ == "__main__":
    open_port(2106)
    open_port(7777)
