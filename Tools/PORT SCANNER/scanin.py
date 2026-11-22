import socket
import ipaddress
import pyfiglet

banner = pyfiglet.figlet_format("SCANIN", font="slant")
print("<--------------------xXx-------------------->")
print(banner)
print("version 1.0")
print("<--------------------xXx-------------------->")
print("\n")

while True:
    host = input("IP > ")

    try:
        ipaddress.IPv4Address(host)
        print("[+] LEGIT\n")
        break

    except ValueError:
        print("[-] NOT LEGIT FORMAT\n")

    
end_port = int(input("end port > "))
print("\n")

open_port = 0
close_port = 0


print("<----------SCANNING START---------->")


def scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    
    result = s.connect_ex((host, port))

    s.close()
   

    if(result == 0):
        print(f"PORT {port}/TCP : [+] OPEN\n")
        return True
    
    else:
        print(f"PORT {port}/TCP : [-] CLOSE\n")
        return False
    
 
for port in range(1, end_port+1):
    if scanner(port):
        open_port += 1
    else:
        close_port += 1

print("<-----------xXx----------->\n")

print(f"[*] Total PORT Scanned  : {end_port}")
print(f"[+] Open PORT : {open_port}")
print(f"[-] Close PORT : {close_port}")
