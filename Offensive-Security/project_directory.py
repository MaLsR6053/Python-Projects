#!/usr/bin/env python3

import os
import re

def sanitize_name(name):
    name = name.strip().replace(' ', '_')
    name = re.sub(r'[^A-Za-z0-9_-]', '', name)
    return name

def create_structure(base_path):
    structure = [
        "EPT/evidence/credentials",
        "EPT/evidence/data",
        "EPT/evidence/screenshots",
        "EPT/logs",
        "EPT/scans",
        "EPT/scope",
        "EPT/tools",
        "IPT/evidence/credentials",
        "IPT/evidence/data",
        "IPT/evidence/screenshots",
        "IPT/logs",
        "IPT/scans",
        "IPT/scope",
        "IPT/tools",
    ]

    for subfolder in structure:
        full_path = os.path.join(base_path, subfolder)
        os.makedirs(full_path, exist_ok=True)
        print(f"[+] Created: {full_path}")

def main():
    print("Project Directory Creator")
    company_name = input("Enter the company or box name: ").strip()
    safe_name = sanitize_name(company_name)

    home = os.path.expanduser("~")
    top_level_dir = os.path.join(home, safe_name)
    os.makedirs(top_level_dir, exist_ok=True)

    create_structure(top_level_dir)

    print(f"\n[+] Done! Your project is under: {top_level_dir}")

if __name__ == "__main__":
    main()
