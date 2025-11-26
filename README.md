🛡️ White Kernel Hunter

The Ultimate Network Reconnaissance Tool > Built for Ethical Hackers, Red Teamers & Bug Bounty Hunters

💀 What is White Kernel Hunter?

White Kernel Hunter is an advanced, multi-threaded command-line interface (CLI) tool designed for high-speed network reconnaissance. Unlike traditional scanners that only tell you if a port is open, White Kernel Hunter performs Deep Banner Grabbing to identify exact software versions (e.g., Apache/2.4.41, OpenSSH 8.2p1, MySQL 8.0).

Written in Python 3, it utilizes threading (500+ threads) to scan all 65,535 ports in minutes, making it a perfect weapon for the Reconnaissance Phase of any penetration test.

🔥 Key Features

🚀 Ultra-Fast Port Scanning: Scans the full port range (1-65,535) using 500 concurrent threads.

🧠 Smart Banner Grabbing: Auto-detects services on HTTP, HTTPS, SSH, FTP, SMTP, and more.

🌐 Subdomain Enumeration: Discovers hidden subdomains (e.g., admin.site.com, dev.site.com).

🛡️ Safety Lock: Enforces usage inside a Virtual Environment to prevent dependency conflicts.

🎨 Hacker-Style Interface: Professional color-coded CLI output using colorama.

📥 Installation
```Get started in seconds. You need Python 3 and Git installed.

# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME_HERE/White-Kernel-Hunter.git](https://github.com/YOUR_USERNAME_HERE/White-Kernel-Hunter.git)

# 2. Navigate to the folder
cd White-Kernel-Hunter

# 3. Create & Activate Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 4. Install Dependencies
pip install -r requirements.txt
```
⚡ Usage
```Run the tool simply by executing the main script:
python main.py
```
🎮 Menu Options

Once launched, choose your attack mode:

[1] Advanced Port Scanner

Input: Target IP or Domain (e.g., scanme.nmap.org).

Action: Scans all ports (1-65535) and identifies running services.

Output:

[+] Port 21 Open : Pure-FTPd [privsep] [TLS]
[+] Port 22 Open : SSH-2.0-OpenSSH_8.0
[+] Port 80 Open : Apache/2.4.18 (Ubuntu)



[2] Subdomain Enum (Basic)

Input: Main Domain (e.g., google.com).

Action: Brute-forces common subdomains to find hidden assets.

Output:

[+] Found: mail.google.com (Status: 200)
[+] Found: admin.google.com (Status: 403)

📸 Screenshots

(Add a screenshot of your tool running here)

⚠️ Disclaimer

White Kernel Hunter is developed for educational and ethical testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

👑 Credits

Lead Developer: Mr Fin

Co-Developer: Mezushi
