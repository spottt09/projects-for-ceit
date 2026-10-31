
#importing socket library 
#and scapy for networking function like hostname resolution and basic networking communication

import socket
from scapy.all import sniff, IP, TCP, UDP, ICMP

#set hostname 

host = socket.gethostname()

#gethostbyname try to resolve the hostname to IPv4 address

try:
	local_ip = socket.gethostbyname(host)

#this part handle error

except socket.gaierror:
	local_ip = 'Cannot resolve your local IP'

#print out the credentials

print(f'Host : {host}')

print(f'Local IP : {local_ip}')

print('Capturing the packets, press Ctrl+C to stop')

#just some bar

print('=' * 25)

#packets identitifying process

def packet_processing(packet):
#it gonna ingnore the packets that don't contain IP layer
	if IP not in packet:
		return

#IP header information depending on ip

	ip_layer = packet[IP]
	source = ip_layer.src
	destination = ip_layer.dst
	protocol_number = ip_layer.proto
	packet_size = len(packet)

#identifying packet type, their sources and destinations, protocol, and size

	if TCP in packet:
		protocol = 'TCP'
	elif UDP in packet:
		protocol = 'UDP'
	elif ICMP in packet:
		protocol = 'ICMP'
	else:
		protocol = f'Other IP protocol{protocol_number}'

#printing out data
	print(f'\nProtocol : {protocol} {protocol_number}')
	print(f'Source : {source}')
	print(f'Destination : {destination}')
	print(f'Packet Size : {packet_size} bytes\n')

try:
	sniff(
		filter='ip',
		prn=packet_processing,
		store=False) #This program doesn't store anything

#to stop when you click something

except KeyboardInterrupt:
	print('Packet Capturing Stopped', flush=True)
