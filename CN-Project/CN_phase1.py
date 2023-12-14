import socket
from _socket import getservbyport

def check_open_ports(host, port_range):
    lower_port, upper_port = port_range
    for port in range(lower_port, upper_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            print(f"Host {host} is online"
                  f" \nrunning on port {port}"
                  f" \nThe service: {getservbyport(port)}"
                  f" \n----------------")
        except socket.error:
            pass

if __name__ == "__main__":

    host = input("Host: ")
    port_range = (int(input("Lower_Port: ")), int(input("Upper_Port: ")))
    check_open_ports(host, port_range)
