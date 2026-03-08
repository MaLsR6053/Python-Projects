import re
import sys

def extract_ports(text):
    # Match lines like '80/tcp open' and extract the port
    ports = re.findall(r'^(\d{1,5})/tcp\s+open', text, re.MULTILINE)
    unique_ports = sorted(set(map(int, ports)))
    return ",".join(map(str, unique_ports))

if __name__ == "__main__":
    print("📥 Paste your port scan output below. Press Ctrl+D (Linux/macOS) or Ctrl+Z + Enter (Windows) when done:\n")

    try:
        input_text = sys.stdin.read()
        port_list = extract_ports(input_text)
        print(f"\n✅ Paste this in your nmap scan:\n\nnmap -p {port_list} <target-ip>\n")
    except Exception as e:
        print(f"❌ Error: {e}")
