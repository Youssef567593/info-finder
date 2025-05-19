#!/usr/bin/env python3
import os
import requests

def ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")

def phone_info(number):
    url = f"https://htmlweb.ru/geo/api.php?json&telcod={number}"
    response = requests.get(url)
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")

def main():
    os.system("clear")
    print("[+] Info Finder Tool")
    print("[1] Find info by IP")
    print("[2] Find info by Phone Number")
    choice = input("Choose option: ")
    
    if choice == "1":
        ip = input("Enter IP address: ")
        ip_info(ip)
    elif choice == "2":
        number = input("Enter phone number: ")
        phone_info(number)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
