# NetworkHealth
# Network Health Monitor

A Python-based network automation tool that performs automated health checks across multiple Cisco IOS devices using Netmiko.

## What it does

- Connects to multiple network devices simultaneously via SSH
- Pulls interface status (up/down) from each device
- Pulls CPU usage from each device
- Reports connection success or failure per device
- Timestamps every health check run

## Tech Stack

- Python 3
- Netmiko 4.7.0
- PyYAML
- Cisco IOSv (GNS3 lab environment)

## Project Structure
network-health/
├── devices.yaml        # device inventory and credentials
├── health_check.py     # main automation script
└── README.md

## How to run

1. Clone the repo
2. Install dependencies
```bash
pip install netmiko pyyaml
```
3. Update devices.yaml with your device IPs and credentials
4. Run the script
```bash
python health_check.py
```

## Sample Output
Network Health Check — 2026-06-08 13:22
Device: R1 | IP: 10.0.0.1
--- Interface Status ---
Interface       IP-Address      OK? Method Status Protocol
GigabitEthernet0/0 10.0.0.1    YES manual up     up
--- CPU Usage ---
CPU utilization for five seconds: 2%
✅ R1 — OK
Device: R2 | IP: 192.168.122.2
✅ R2 — OK
Device: R3 | IP: 10.0.0.10
✅ R3 — OK

## Lab Environment

Built and tested on a GNS3 lab running Cisco IOSv routers on EndeavourOS (Arch Linux).

## Author

Anubhav Shrestha
