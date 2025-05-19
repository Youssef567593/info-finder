#!/data/data/com.termux/files/usr/bin/python3
import requests

def ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url).json()
    print("\n--- IP Information ---")
    for k, v in res.items():
        print(f"{k} : {v}")

def phone_info(phone):
    url = f"https://numlookupapi.com/api/validate/{phone}"
    res = requests.get(url).json()
    print("\n--- Phone Number Information ---")
    for k, v in res.items():
        print(f"{k} : {v}")

print("1 - Get IP Information")
print("2 - Get Phone Number Information")
choice = input("Choose (1 or 2): ")

if choice == "1":
    ip = input("Enter IP address: ")
    ip_info(ip)

elif choice == "2":
    phone = input("Enter phone number with country code (e.g., +213...): ")
    phone_info(phone)

else:
    print("Invalid choice.")
