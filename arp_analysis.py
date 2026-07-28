from scapy.all import rdpcap, ARP

packets = rdpcap("arp_spoofing_lab.pcap")

arp_packets = [pkt for pkt in packets if pkt.haslayer(ARP)]

ip_mac_map = {}
gratuitous = []

for pkt in arp_packets:
    ip = pkt[ARP].psrc
    mac = pkt[ARP].hwsrc

    if ip not in ip_mac_map:
        ip_mac_map[ip] = set()
    ip_mac_map[ip].add(mac)

    if pkt[ARP].psrc == pkt[ARP].pdst:
        gratuitous.append(ip)

print("\n--- IP to MAC Mapping ---")
for ip, macs in ip_mac_map.items():
    print(f"{ip} → {', '.join(macs)}")

print("\n--- Duplicate IPs ---")
for ip, macs in ip_mac_map.items():
    if len(macs) > 1:
        print(f"[!] Suspicious: {ip} → {macs}")

print("\n--- Gratuitous ARP ---")
for ip in set(gratuitous):
    print(f"Gratuitous ARP from {ip}")

print("\n--- Spoofing Assessment ---")
flag = False

for ip, macs in ip_mac_map.items():
    if len(macs) > 1:
        print(f"[WARNING] {ip} has multiple MACs: {macs}")
        flag = True

if not flag:
    print("No strong ARP spoofing detected.")