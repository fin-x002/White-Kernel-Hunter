# White Kernel Hunter

## Overview
White Kernel Hunter is a professional Python CLI network reconnaissance tool designed for security testing and network analysis. The tool provides advanced port scanning with banner grabbing capabilities and subdomain enumeration.

**Leaders:** Babu & Mezushi

## Features
- **Virtual Environment Detection:** Ensures the tool runs only in isolated environments for security
- **Advanced Port Scanner:** Multi-threaded (100 threads) port scanning with service banner detection
- **Banner Grabbing:** Identifies service versions and details on open ports
- **Subdomain Enumeration:** Discovers active subdomains using common wordlists
- **Professional CLI:** Styled with colorful ASCII banners and formatted output

## Project Structure
```
.
├── main.py              # Main CLI application
├── requirements.txt     # Python dependencies
└── replit.md           # Project documentation
```

## Dependencies
- `colorama` - Terminal color formatting
- `requests` - HTTP requests for subdomain checking
- Built-in: `socket`, `threading`, `sys`, `os`

## Usage
The tool must be run inside a virtual environment. Upon launch, it displays an ASCII banner and presents a main menu with three options:

1. **Advanced Port Scanner** - Scans specified port ranges with banner grabbing
2. **Subdomain Enumeration** - Discovers active subdomains
3. **Exit** - Closes the application

## Recent Changes
- 2025-11-26: Initial project creation with all core features implemented

## Architecture Notes
- Multi-threaded architecture using Python's threading module
- Queue-based port scanning for efficient resource management
- Thread-safe output using locks for concurrent operations
- Graceful error handling with try-except blocks throughout
