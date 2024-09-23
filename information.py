import requests
import os
import sys
import time


def print_colored_banner():
    banner = r"""
  _   _ _  _   _             _____        __                           _   _                _____       _   _               _             
 | \ | | || | | |           |_   _|      / _|                         | | (_)              / ____|     | | | |             (_)            
 |  \| | || |_| |_ ________   | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __   | |  __  __ _| |_| |__   ___ _ __ _ _ __   __ _ 
 | . ` |__   _| __|_  /_  /   | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \  | | |_ |/ _` | __| '_ \ / _ \ '__| | '_ \ / _` |
 | |\  |  | | | |_ / / / /   _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | | | |__| | (_| | |_| | | |  __/ |  | | | | | (_| |
 |_| \_|  |_|  \__/___/___| |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|  \_____|\__,_|\__|_| |_|\___|_|  |_|_| |_|\__, |
                                                                                                                                     __/ |
                                                                                                                                    |___/ 
"""
    
    colors = [31, 32, 33, 34, 35, 36] 
    for i in range(len(banner.splitlines())):
        print(f"\033[1;{colors[i % len(colors)]}m{banner.splitlines()[i]}\033[0m")
        time.sleep(0.1)

def get_whois(domain):
    response = requests.get(f'https://api.whois.vu/?q={domain}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    print_colored_banner()
    domain = input("Domain (Use IP) : ")
    whois_info = get_whois(domain)

    if whois_info:
        print("\nInformasi WHOIS:")
        print(whois_info)
    else:
        print("Not Get Informations!.")
