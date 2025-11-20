import socket
import whois
import requests

domain = input("Domain veya IP girin: ")

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Adresi: {ip}")
        return ip
    except:
        print("[-] Domain çözülemedi!")
        return None

def ip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url).json()

        print("\n--- IP Bilgileri ---")
        print(f"Ülke: {data['country']}")
        print(f"Şehir: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"Organizasyon: {data['org']}")
        print(f"Zaman Dilimi: {data['timezone']}")
    except:
        print("IP bilgisi alınamadı!")

def whois_lookup(domain):
    try:
        w = whois.whois(domain)

        print("\n--- WHOIS Bilgileri ---")
        print(f"Registrar: {w.registrar}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Domain Oluşturulma: {w.creation_date}")
        print(f"Domain Bitiş Tarihi: {w.expiration_date}")
    except:
        print("WHOIS bilgisi alınamadı!")



if not domain.replace(".", "").isdigit():
    ip = domain_to_ip(domain)
    if ip:
        ip_lookup(ip)
        whois_lookup(domain)


else:
    ip_lookup(domain)
