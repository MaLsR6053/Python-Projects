import dns.resolver

def find_subdomains(domain, subdomains):
    for subdomain in subdomains:
        target = f"{subdomain}.{domain}"
        try:
            result = dns.resolver.resolve(target)
            print(f"Here is a subdomain that I found: {target}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"Subdomain not found: {target}")

domain = input("Enter the domain (e.g., http://hackerzrule.com): ")
subdomains = ["www", "mail", "ftp", "dev", "blog", "test"]  # Add more subdomains to this list. But once again, this needs to be updated to allow adding of a text file.

find_subdomains(domain, subdomains)
