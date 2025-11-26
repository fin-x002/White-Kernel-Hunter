#!/usr/bin/env python3
import sys
import os

# --- Virtual Environment Check ---
def check_virtual_env():
    # Replit-e environment check skip kora hoy
    if os.getenv('REPL_ID') or os.getenv('REPLIT_DB_URL'):
        return
    
    # Check if running in venv
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        try:
            from colorama import Fore, Style, init
            init(autoreset=True)
            print(Fore.RED + "Error: Please run this tool inside a virtual environment!" + Style.RESET_ALL)
        except ImportError:
            print("Error: Please run this tool inside a virtual environment!")
        sys.exit(1)

check_virtual_env()

# --- Library Import with Error Handling ---
try:
    import socket
    import threading
    import requests
    from colorama import Fore, Style, Back, init
    import time
    from queue import Queue
except ImportError as e:
    print(f"Error: Missing required library - {e.name}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

init(autoreset=True)

# --- Utility Functions ---
def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def display_banner():
    clear_screen()
    banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════╗
║             White Kernel Hunter               ║
║         Advanced Reconnaissance Tool          ║
║             Leader: Babu & Mezushi            ║
╚═══════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

# --- Port Scanner Class ---
class PortScanner:
    def __init__(self, target, start_port=1, end_port=65535, threads=500):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.queue = Queue()
        self.open_ports = []
        self.lock = threading.Lock()
        
    def grab_banner(self, port):
        """
        Advanced Banner Grabbing Logic
        Sends specific triggers based on the port number.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((self.target, port))
            
            # Web Ports (HTTP)
            if port in [80, 8080, 3000, 8000, 8008]:
                msg = f"GET / HTTP/1.1\r\nHost: {self.target}\r\n\r\n".encode('utf-8')
                sock.send(msg)
            
            # Secure Web Port (HTTPS)
            elif port == 443:
                sock.close()
                return "HTTPS Web Server (Encrypted)"
            
            # FTP / SSH / Telnet / SMTP (Standard Handshake)
            else:
                # Kichu server prothomkei kotha bole (SSH/FTP), kichu server wait kore
                # Amra ektu wait kore dekhi tara kotha bole kina
                pass 
            
            # Receive Data
            try:
                # Kichu data na ashle 'Unknown' return korbe
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                sock.close()
                return banner if banner else "Unknown Service (No Banner)"
            except:
                # Jodi receive timeout hoy, tar mane server chup chap ache
                # Amra tokhon 'Hello' pathiye abar try korte pari (Optional)
                sock.close()
                return "Unknown Service"
                
        except:
            return None
    
    def scan_port(self):
        while not self.queue.empty():
            port = self.queue.get()
            try:
                # Check if Port is Open
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                
                if result == 0:
                    # Port is Open! Now Grab Banner.
                    # Note: We create a NEW connection for banner grabbing to be safe
                    banner = self.grab_banner(port)
                    
                    with self.lock:
                        self.open_ports.append((port, banner))
                        # Live Output
                        print(Fore.GREEN + f"[+] Port {port} Open : {banner}")
                
                sock.close()
            except:
                pass
            finally:
                self.queue.task_done()
    
    def run(self):
        print(Fore.YELLOW + f"\n[*] Starting scan on {self.target}")
        print(Fore.YELLOW + f"[*] Scanning ports {self.start_port}-{self.end_port}...")
        print(Fore.YELLOW + f"[*] Using {self.threads} threads for maximum speed\n")
        
        # Queue fill kora
        for port in range(self.start_port, self.end_port + 1):
            self.queue.put(port)
        
        # Threads start kora
        thread_list = []
        for _ in range(self.threads):
            thread = threading.Thread(target=self.scan_port)
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        # Wait for threads to finish
        for thread in thread_list:
            thread.join()
        
        print(Fore.CYAN + f"\n[*] Scan completed! Found {len(self.open_ports)} open ports.")

# --- Subdomain Scanner Class ---
class SubdomainScanner:
    def __init__(self, domain):
        self.domain = domain
        # Common Subdomains List
        self.subdomains = [
            'www', 'mail', 'remote', 'blog', 'webmail', 'server',
            'admin', 'ftp', 'smtp', 'pop', 'ns1', 'ns2', 'test',
            'vpn', 'api', 'dev', 'staging', 'portal', 'app',
            'dashboard', 'cpanel', 'whm', 'shop', 'store', 'secure'
        ]
        self.found = []
    
    def check_subdomain(self, subdomain):
        url = f"http://{subdomain}.{self.domain}"
        try:
            # Request pathano (3 sec timeout)
            response = requests.get(url, timeout=3, allow_redirects=True)
            if response.status_code in [200, 403, 301, 302]:
                self.found.append(subdomain)
                print(Fore.GREEN + f"[+] Found: {subdomain}.{self.domain} (Status: {response.status_code})")
        except:
            pass
    
    def run(self):
        print(Fore.YELLOW + f"\n[*] Starting subdomain enumeration for {self.domain}")
        print(Fore.YELLOW + f"[*] Testing {len(self.subdomains)} common subdomains...\n")
        
        threads = []
        for subdomain in self.subdomains:
            thread = threading.Thread(target=self.check_subdomain, args=(subdomain,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(Fore.CYAN + f"\n[*] Scan completed! Found {len(self.found)} subdomains.")

# --- Menus ---
def port_scanner_menu():
    print(Fore.YELLOW + "\n=== Advanced Port Scanner ===")
    target = input(Fore.WHITE + "Enter Target IP/Domain: ").strip()
    
    if not target:
        print(Fore.RED + "[!] Target cannot be empty!")
        return
    
    try:
        # Resolve Domain to IP
        target_ip = socket.gethostbyname(target)
        print(Fore.CYAN + f"[*] Resolved {target} to {target_ip}")
    except socket.gaierror:
        print(Fore.RED + f"[!] Could not resolve hostname: {target}")
        return
    
    try:
        # Auto-scan all ports
        scanner = PortScanner(target_ip)
        scanner.run()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Scan interrupted by user.")

def subdomain_scanner_menu():
    print(Fore.YELLOW + "\n=== Subdomain Enumeration ===")
    domain = input(Fore.WHITE + "Enter Target Domain (e.g., google.com): ").strip()
    
    if not domain:
        print(Fore.RED + "[!] Domain cannot be empty!")
        return
    
    try:
        scanner = SubdomainScanner(domain)
        scanner.run()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Scan interrupted by user.")

def main_menu():
    while True:
        print(Fore.CYAN + "\n=== Main Menu ===")
        print(Fore.WHITE + "[1] Advanced Port Scanner (with Banner Grabbing)")
        print(Fore.WHITE + "[2] Subdomain Enum (Basic)")
        print(Fore.WHITE + "[3] Exit")
        
        choice = input(Fore.YELLOW + "\nSelect an option: ").strip()
        
        if choice == '1':
            port_scanner_menu()
        elif choice == '2':
            subdomain_scanner_menu()
        elif choice == '3':
            print(Fore.GREEN + "\n[*] Exiting White Kernel Hunter. Stay safe!")
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice! Please select 1, 2, or 3.")

def main():
    try:
        display_banner()
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Program interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()