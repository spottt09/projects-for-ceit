# This is the First version of sniffer.py

from scapy.all import sniff, IP

def show_packet(packet):
	print('Packet received:', packet.summary(), flush=True)

	if IP in packet:
		print('source:', packet[IP].src, flush=True)

		print('destination:', packet[IP].dst, flush=True)

print('start capturing on eth0', flush=True)

sniff(iface='eth0', filter='ip', prn=show_packet, store=False)
