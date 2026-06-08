import yaml
from netmiko import ConnectHandler
from datetime import datetime

# Load devices from YAML
with open("devices.yaml") as f:
    config = yaml.safe_load(f)

devices = config["devices"]

# Timestamp for report
today = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"\nNetwork Health Check — {today}")
print("=" * 40)

# Loop through every device
for device in devices:
    print(f"\nDevice: {device['name']} | IP: {device['hostname']}")
    
    try:
        # Connect via Netmiko
        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["hostname"],
            username=device["username"],
            password=device["password"]
        )

        # Pull interface status
        output = connection.send_command("show ip interface brief")
        print("--- Interface Status ---")
        print(output)

        # Pull CPU usage
        cpu = connection.send_command("show processes cpu | include CPU")
        print("--- CPU Usage ---")
        print(cpu)

        connection.disconnect()
        print(f"✅ {device['name']} — OK")

    except Exception as e:
        print(f"❌ {device['name']} — FAILED: {e}")

print("\nHealth check complete.")
