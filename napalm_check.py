import yaml
from napalm import get_network_driver
from datetime import datetime

# Load devices
with open("devices.yaml") as f:
    config = yaml.safe_load(f)

devices = config["devices"]

today = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"\nNAPALM Health Check — {today}")
print("=" * 40)

for device in devices:
    print(f"\nDevice: {device['name']} | IP: {device['hostname']}")
    
    try:
        driver = get_network_driver("ios")
        
        conn = driver(
            hostname=device["hostname"],
            username=device["username"],
            password=device["password"],
	    optional_args={
		"secret": device["secret"],
		"conn_timeout": 60,
		"read_timeout_override": 60
		}
        )
        
        conn.open()
        
        # Get structured interface data
        interfaces = conn.get_interfaces()
        
        print("--- Interface Status ---")
        for name, data in interfaces.items():
            status = "UP" if data["is_up"] else "DOWN"
            print(f"  {name}: {status}")
            
            # Automatic warning if down
            if not data["is_up"]:
                print(f"  ⚠️  WARNING: {name} is DOWN")
        
        conn.close()
        print(f"✅ {device['name']} — OK")
        
    except Exception as e:
        print(f"❌ {device['name']} — FAILED: {e}")

print("\nHealth check complete.")
