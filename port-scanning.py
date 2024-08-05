import socket

def prt_scanner(target, ports):
    try:
        print(f"Resolving hostname {target}...")
        ip_address = socket.gethostbyname(target)
        print(f"Scanning {target} ({ip_address})")

        for port in ports:
            print(f"Checking port {port}...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
            sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter the domain or IP to scan: ")
    ports_input = input("Enter the ports to scan (comma-separated, or leave blank for default ports): ")
    
    if ports_input:
        ports = [int(port.strip()) for port in ports_input.split(",")]
    else:
        # Lista de portas principais
        ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

    prt_scanner(target, ports)



    ## abelharainha.com.br