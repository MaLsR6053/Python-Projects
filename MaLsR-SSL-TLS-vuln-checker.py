import ssl
import socket

def check_ssl_vulnerabilities(target):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=target)
    conn.settimeout(5)
    
    try:
        conn.connect((target, 443))  # Connecting on the HTTPS port
        print(f"Yay! SSL/TLS connection to {target} successful!")
    except Exception as e:
        print(f"Boooooo. The SSL/TLS connection failed for {target}: {e}")
    finally:
        conn.close()

target = input("Enter a domain (e.g. http://hackerzrule.com) to check SSL/TLS vulnerabilities: ")
check_ssl_vulnerabilities(target)
