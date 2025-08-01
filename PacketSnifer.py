from scapy.all import sniff, wrpcap

# Capture 20 packets
print("Sniffing packets... please wait.")
packets = sniff(count=20)

# Save to a .pcap file
wrpcap("my_capture.pcap", packets)

print("✅ Packets saved to my_capture.pcap")