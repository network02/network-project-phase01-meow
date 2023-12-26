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

def check_host_online(host, port):
    try:
        socket.create_connection((host, port))
        return True
    except socket.error:
        return False

def post_get(request):

    server_address = ("127.0.0.1", 8080)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)


    data = request
    client_socket.sendall(data.encode())
    response = client_socket.recv(1024).decode()
    print("Server response:", response)
    client_socket.close()


if __name__ == "__main__":

    action = input("What do you want to do?"
                   "\n 1.Check if the host is online"
                   "\n 2.Check open ports and its services"
                   "\n 3.GET or POST Request\n")
    match action:
        case "1":
            host = input("Host: ")
            port = input("Port: ")
            is_host_online = check_host_online(host, port)
            if is_host_online:
                print("Host is online.")
            else:
                print("Host is offline.")
        case "2":
            host = input("Host: ")
            port_range = (int(input("Lower_Port: ")), int(input("Upper_Port: ")))
            check_open_ports(host, port_range)
        case "3":
            while(True):
                post_get(input("Enter 'GET user_id' or 'POST name age': "))

