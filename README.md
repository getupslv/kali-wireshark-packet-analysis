# Network Security & Packet Analysis Sandbox

A hands-on cybersecurity project focused on monitoring network traffic, analyzing packet captures, and automating defensive security tasks using a secure virtual environment.

## Tools & Technologies Used
* **Operating System:** Kali Linux
* **Network Analysis:** Wireshark
* **Automation:** Python

## Project Core Tasks
* **Environment Setup:** Configured a secure sandbox environment using Kali Linux to capture and evaluate network protocols safely.
* **Traffic Analysis:** Monitored live traffic using Wireshark, applying display filters to isolate TCP handshakes, DNS queries, and potential network anomalies.
* **Security Automation:** Wrote custom Python scripts to parse text-based logs, automatically filtering out safe traffic to pinpoint unencrypted or high-risk protocols.
## Script Spotlight: Python Log Parser
Included in this repository is `log_parser.py`, a script designed to automatically parse text-based network captures (`network_log.txt`) and trigger immediate alerts whenever unencrypted HTTP traffic is detected. 
