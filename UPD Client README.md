# UDP Client Script

This script demonstrates how to create a simple UDP client using Python's `socket` module. It sends a small message to a specified target host and port, then listens for and prints the response.

## Features
- Establishes a connection to a specified server using the UDP protocol.
- Sends a predefined message (`"AAABBBCCC"`) to the target server.
- Receives and displays the server's response.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of networking concepts, including IP addresses and ports.

## How to Use
1. Clone or download this script to your local machine.
2. Open the script in any text editor or IDE.
3. Modify the following variables:
   - `target_host`: Replace `"insert IP address here"` with the IP address of the target server.
   - `target_port`: Replace `XXXX` with the target port number.
4. Run the script using Python:
   ```bash
   python udp_client.py
   ```
5. Observe the server's response printed in the terminal.

## Example Usage
If your server is hosted locally and listening on port 8080:
```python
target_host = "127.0.0.1"
target_port = 8080
```

## Notes
- Ensure the server you are targeting is configured to receive UDP packets on the specified port.
- The message sent (`"AAABBBCCC"`) can be customized by editing the `client.sendto` line in the script.
- UDP does not guarantee delivery, order, or duplicate protection, so the script may not receive a response under certain network conditions.

## Disclaimer
Use this script responsibly. Ensure you have proper authorization before sending packets to any network or server.

