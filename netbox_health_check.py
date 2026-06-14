import requests
from netmiko import ConnectHandler
from datetime import datetime

# NetBox connection details
NETBOX_URL = "http://localhost:8000"
NETBOX_TOKEN = "nbt_2pfE0P3CWJPs.puI7KjoG1Nh4ez9AaUHCwM7M64RALSDkZztQxba5"

headers = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}

# Pull devices from NetBox API
response = requests.get(
    f"{NETBOX_URL}/api/dcim/devices/",
    headers=headers
)

data = response.json()
devices = data["results"]

# Timestamp
today = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"\nNetBox Health Check — {today}")
print("=" * 40)

for device in devices:
    # Get device name and primary IP from NetBox
    name = device["name"]
    
    # Skip if no primary IP assigned
    if not device["primary_ip"]:
        print(f"\n⚠️  {name} — No primary IP in NetBox, skipping")
        continue
    
    # Extract just the IP without the /prefix
    ip = device["primary_ip"]["address"].split("/")[0]
    
    print(f"\nDevice: {name} | IP: {ip}")
    
    try:
        connection = ConnectHandler(
            device_type="cisco_ios",
            host=ip,
            username="admin",
            password="cisco123",
            secret="cisco123"
        )
        
        output = connection.send_command("show ip interface brief")
        print("--- Interface Status ---")
        print(output)
        
        connection.disconnect()
        print(f"✅ {name} — OK")
        
    except Exception as e:
        print(f"❌ {name} — FAILED: {e}")

print("\nHealth check complete.")
