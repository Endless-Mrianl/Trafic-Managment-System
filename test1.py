import time

# Function to simulate vehicle detection during green light
def detect_vehicles_during_green_light():
    # Simulated vehicle count
    vehicle_count = 0
    # Simulate detecting vehicles for 5 seconds
    for _ in range(5):
        # Detect vehicles (simulated)
        # Increment vehicle count (simulated)
        vehicle_count += 1
        time.sleep(1)  # Simulate processing time
    return vehicle_count

# Function to simulate traffic light control
def simulate_traffic_light():
    # Simulated initial vehicle count
    initial_vehicle_count = detect_vehicles_during_green_light()
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Simulated vehicle count after 5 seconds
    final_vehicle_count = detect_vehicles_during_green_light()
    
    # Check if vehicle count remains the same after 5 seconds
    if initial_vehicle_count == final_vehicle_count:
        # Wait for additional 5 seconds
        time.sleep(5)
        # Simulated vehicle count after additional 5 seconds
        final_vehicle_count_10_seconds = detect_vehicles_during_green_light()
        # If vehicle count still same, change light to red
        if initial_vehicle_count == final_vehicle_count_10_seconds:
            print("Turning light to red after 10 seconds")
            # Code to change traffic light to red (simulated)
        else:
            print("Vehicle count changed within 10 seconds, turning light to red immediately")
            # Code to change traffic light to red (simulated)
    else:
        print("Vehicle count changed within 5 seconds, turning light to red immediately")
        # Code to change traffic light to red (simulated)

# Simulate traffic light control
simulate_traffic_light()
