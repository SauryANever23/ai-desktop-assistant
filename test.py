from pydbus import SystemBus
import time

DEVICE_MAC = "48:f1:7f:f0:e5:6f"  # Replace with your device MAC

bus = SystemBus()
manager = bus.get("org.bluez", "/")

# Get Bluetooth adapter (usually hci0)
adapter_path = "/org/bluez/hci0"
adapter = bus.get("org.bluez", adapter_path)

# Start discovery
adapter.StartDiscovery()
print("Discovering devices...")
time.sleep(5)  # Allow time for discovery
adapter.StopDiscovery()

# Format device path
device_path = f"{adapter_path}/dev_{DEVICE_MAC.replace(':', '_')}"
device = bus.get("org.bluez", device_path)

# Trust the device
device.Trusted = True

# Pair the device if not paired
if not device.Paired:
    print("Pairing...")
    device.Pair()
    print("Paired.")

# Connect
print("Connecting...")
device.Connect()
print("Connected.")
