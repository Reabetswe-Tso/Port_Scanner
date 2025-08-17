# Simple Port Scanner

A basic Python-based port scanner that allows you to check whether common ports on a host are open or closed. This project uses the `socket` module to attempt TCP connections to target ports.

---

## Features

- Scan a target host (domain or IP) for common ports.
- Detects whether each port is **OPEN**, **CLOSED**, or **ERROR**.
- Timeout support for faster scanning.
- Easy to expand by adding more ports.

---

## Technologies Used

- Python 3
- `socket` module

---

## Installation

1. Make sure you have Python 3 installed.
2. Clone this repository or download the script.
3. Run the script using the command:

```bash
python port_scanner.py
```
## Usage

1. Run the script.

2. Enter the host you want to scan. E.g Enter host (e.g., scanme.nmap.org or 127.0.0.1): 

3. The scanner will check the following common ports by default: 20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306

4. The output will display the status of each port:
   Port 22: OPEN
   Port 80: CLOSED
   Port 443: OPEN

## Notes

- Make sure you have permission to scan the target host. Unauthorized scanning may be illegal.

- The script uses a 1-second timeout to speed up scanning.
  
## Author
Reabetswe Tsotetsi
  
