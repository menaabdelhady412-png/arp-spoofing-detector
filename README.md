# arp-spoofing-detector
ARP traffic analysis and spoofing detection using Python and Scapy.
# ARP Analysis & Spoofing Detection using Python and Scapy

## Overview

This project demonstrates the analysis of Address Resolution Protocol (ARP) traffic using **Python** and **Scapy** to identify network anomalies and detect potential **ARP spoofing attacks**. The analysis was performed on a packet capture (PCAP) from a simulated local area network to investigate suspicious ARP behavior and assess the integrity of IP-to-MAC address mappings.

The project focuses on applying network security concepts through automated packet analysis, helping identify indicators of ARP poisoning that could impact communication within a LAN.

---

## Objectives

* Parse ARP packets from a PCAP file using Scapy.
* Extract and summarize IP-to-MAC address mappings.
* Detect duplicate IP address mappings.
* Identify Gratuitous ARP packets.
* Flag potential ARP spoofing or poisoning attempts.
* Produce a clear security assessment based on the observed traffic.

---

## Technologies Used

* Python 
* Scapy
* PCAP Analysis
* Address Resolution Protocol (ARP)
* Network Security

---

## Features

* Reads and processes ARP packets from a PCAP file.
* Builds a complete IP-to-MAC mapping table.
* Detects duplicate IP addresses associated with multiple MAC addresses.
* Identifies Gratuitous ARP announcements.
* Separates normal observations from suspicious activity.
* Generates clear, readable output suitable for security analysis.

---

## Project Structure

```text
ARP-Spoofing-Detection/
│
├── arp_analysis.py
├── arp_spoofing_lab.pcap
├── README.md
├── report/
│   └── ARP_Analysis_Report.pdf
│
└── screenshots/
    ├── mappings.png
    └── output.png
```

---

## How It Works

The script loads the provided PCAP file using Scapy and processes every ARP packet encountered during the capture.

For each packet, the program:

* Extracts the sender IP and MAC address.
* Builds a mapping table of observed devices.
* Detects duplicate IP-to-MAC mappings.
* Identifies Gratuitous ARP announcements.
* Evaluates whether conflicting mappings indicate potential ARP spoofing.

The final output distinguishes legitimate network activity from suspicious behavior and provides evidence supporting the analysis.

---

## Example Output

```
========== IP to MAC Mapping ==========

192.168.1.1   -> 00:11:22:33:44:55
192.168.1.10  -> AA:BB:CC:DD:EE:01
192.168.1.20  -> AA:BB:CC:DD:EE:02

========== Duplicate IP Detection ==========

WARNING:
192.168.1.10
AA:BB:CC:DD:EE:01
11:22:33:44:55:66

========== Gratuitous ARP ==========

192.168.1.15 announced its own mapping.

========== Security Assessment ==========

Potential ARP spoofing activity detected due to conflicting MAC addresses associated with the same IP address.
```

---

## Skills Demonstrated

* Network Traffic Analysis
* ARP Protocol Analysis
* Packet Capture (PCAP) Processing
* Python Scripting
* Scapy
* Cybersecurity Fundamentals
* Layer 2 Networking
* Network Threat Detection
* Security Analysis
* Technical Reporting

---

## Learning Outcomes

Through this project, I strengthened my understanding of Layer 2 networking by analyzing ARP communication, identifying abnormal network behavior, and implementing automated detection techniques using Python. The project demonstrates practical application of packet analysis and reinforces fundamental concepts used in network security and Security Operations Center (SOC) environments.

---

## Future Improvements

* Live ARP monitoring instead of offline PCAP analysis.
* Real-time alert generation for detected anomalies.
* Export results to CSV or JSON.
* Interactive visualization of IP-to-MAC relationships.
* Support for additional network anomaly detection techniques.

---

## Author

**Mena Mohamed Sultan**

Cybersecurity Student
Faculty of Computers and Artificial Intelligence, Cairo University

LinkedIn: *https://www.linkedin.com/in/mena-sultan218/*

GitHub: *https://github.com/menaabdelhady412-png*
