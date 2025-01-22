# [TCP Client Script](https://github.com/MaLsR6053/Python-Projects/blob/main/Python%20TCP%20Client.py)

This script demonstrates how to create a simple TCP client using Python's socket module. It connects to a specified target host and port, sends a basic HTTP GET request, and prints the server's response.

## Features
- Establishes a connection to a specified server using the TCP protocol (IPv4).
- Sends an HTTP GET request to the server, requesting the root page (`/`).
- Receives and displays the HTTP response from the server.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of networking concepts, including IP addresses, ports, and HTTP requests.

## How to Use
1. Clone or download this script to your local machine.
2. Open the script in any text editor or IDE.
3. Modify the following variables:
   - `target_host`: Replace `"insert FQDN here"` with the Fully Qualified Domain Name (FQDN) or IP address of the target server.
   - `target_port`: Replace `80` with the desired port number (the default is set to HTTP port 80).
4. Run the script using Python:
   ```bash
   python tcp_client.py
5. Observe the server's response printed in the terminal.

## Example Usage
  If your server is hosted locally and listening on port 80:
```bash
target_host = "127.0.0.1"
target_port = 80
```
## Notes
- The HTTP request sent in this script is a simple GET request, and the response is printed to the console.
- If the target server does not support HTTP or is using a different protocol, this request may fail to produce a meaningful response.
- You can modify the request by changing the client.send() line in the script.
- This script works with servers that accept connections on the TCP protocol, typically used for HTTP servers.

## Disclaimer
Use this script responsibly. Ensure you have proper authorization before sending requests to any server or network. Unauthorized scanning or access may be illegal depending on your jurisdiction.
