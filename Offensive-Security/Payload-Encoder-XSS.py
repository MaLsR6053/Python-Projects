import html

def encode_payload(payload):
    encoded_payload = html.escape(payload)
    print(f"Encoded Payload: {encoded_payload}")

payload = input("Enter your XSS payload: ")
encode_payload(payload)
