import cv2
import time

# Function to detect vehicles using OpenCV
def detect_vehicles(frame):
    # Convert frame to grayscale (for better vehicle detection)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Use a pre-trained vehicle detection model or technique
    # (e.g., Haar cascades, deep learning-based models like YOLO or SSD)
    # to detect vehicles in the frame
    # Detected vehicles will be stored in the 'vehicles' list
    vehicles = []  # Placeholder for detected vehicles
    # Initialize Haar cascade classifier with the car cascade XML file
    car_cascade = cv2.CascadeClassifier('C:/Users/asus/Desktop/25-may/haarcascade_car.xml')
    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray_frame, 1.1, 1)
    for (x, y, w, h) in cars:
        # Draw rectangles around detected vehicles (optional)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # Store the detected vehicles
        vehicles.append((x, y, x + w, y + h))
    return frame, len(vehicles)

# Function to simulate vehicle detection during green light
def detect_vehicles_during_green_light(video_capture):
    # Simulated vehicle count
    vehicle_count = 0
    # Start time for green light duration
    start_time = time.time()
    # Simulate detecting vehicles for 5 seconds
    while (time.time() - start_time) < 5:
        # Read frame from video stream
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to read frame")
            break
        # Detect vehicles in the frame
        frame, count = detect_vehicles(frame)
        # Increment vehicle count
        vehicle_count += count
        # Simulate processing time (optional)
        # time.sleep(0.1)  # Adjust processing time as needed
        # Display the frame (optional)
        cv2.imshow('Frame', frame)
        cv2.waitKey(1)
    return vehicle_count

# Function to simulate traffic light control
def simulate_traffic_light():
    # Access the live video stream (change the video source as needed)
    video_capture = cv2.VideoCapture(r'C:/Users/asus/Desktop/25-may/WhatsApp Video 2024-05-18 at 15.28.33_f4407fea.mp4')

    # Check if video stream opened successfully
    if not video_capture.isOpened():
        print("Error: Unable to open video stream")
        return

    # Simulated initial vehicle count during green light
    initial_vehicle_count = detect_vehicles_during_green_light(video_capture)

    # Wait for 5 seconds
    time.sleep(5)

    # Simulated vehicle count after 5 seconds
    final_vehicle_count = detect_vehicles_during_green_light(video_capture)

    # Release video capture object
    video_capture.release()
    cv2.destroyAllWindows()

    # Check if vehicle count remains the same after 5 seconds
    if initial_vehicle_count == final_vehicle_count:
        # Wait for additional 5 seconds
        time.sleep(5)
        final_vehicle_count_10_seconds = detect_vehicles_during_green_light(video_capture)
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
