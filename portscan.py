import socket
import sys

def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print(f"[+] {port} open")
            client.close()
    except Exception as error:
        print("Error: ", error)

def print_usage():
    print("Usage:")
    print("  python portscan.py <host>                             - Scans common ports for <host>")
    print("  python portscan.py <host> <port>                       - Scans a single port for <host>")
    print("  python portscan.py <host> <port1>,<port2>,<port3>...   - Scans multiple ports for <host>")
    print()
    print("Examples:")
    print("  python portscan.py google.com")
    print("  python portscan.py google.com 80")
    print("  python portscan.py google.com 80,443,8080")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(',')
        else:
            ports = [22, 80, 443, 21, 25, 110, 143, 53, 3306, 5432, 8080, 3389, 445, 8000, 8008, 8888]

        scan(host, ports)
    else:
        print_usage()



