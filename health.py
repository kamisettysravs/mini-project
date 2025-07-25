import csv
import random
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Simulate sensor readings
def read_heart_rate():
    return random.randint(60, 100)  # Heart rate in beats per minute

def read_blood_pressure():
    systolic = random.randint(90, 140)  # Systolic pressure in mmHg
    diastolic = random.randint(60, 90)  # Diastolic pressure in mmHg
    return systolic, diastolic

def read_temperature():
    return round(random.uniform(36.5, 37.5), 1)  # Body temperature in Celsius

# Function to log data to a CSV file
def log_health_data_to_csv(filename="health_data.csv"):
    # Open the CSV file (in append mode)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers if the file is empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Heart Rate (bpm)", "Blood Pressure Systolic (mmHg)", 
                             "Blood Pressure Diastolic (mmHg)", "Temperature (°C)"])
        
        # Read simulated sensor data
        heart_rate = read_heart_rate()
        systolic, diastolic = read_blood_pressure()
        temperature = read_temperature()
        
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Write data to CSV
        writer.writerow([timestamp, heart_rate, systolic, diastolic, temperature])
        
        return f"Data logged at {timestamp}: Heart Rate={heart_rate} bpm, BP={systolic}/{diastolic} mmHg, Temp={temperature} °C"

# Function to simulate periodic logging of health data (e.g., every 10 seconds)
def simulate_health_monitoring(interval_seconds=10, duration_minutes=1):
    duration_seconds = duration_minutes * 60
    num_cycles = duration_seconds // interval_seconds
    
    for _ in range(num_cycles):
        log_message = log_health_data_to_csv()  # Log data to CSV file
        update_log_display(log_message)  # Update the display with the logged message
        time.sleep(interval_seconds)  # Wait before the next logging

# Update the log display
def update_log_display(message):
    log_text.insert(tk.END, message + "\n")
    log_text.yview(tk.END)  # Scroll to the end to show the latest entry

# Start the health monitoring simulation
def start_monitoring():
    try:
        interval_seconds = int(interval_entry.get())
        duration_minutes = int(duration_entry.get())
        if interval_seconds <= 0 or duration_minutes <= 0:
            raise ValueError("Interval and Duration must be positive integers.")
        
        start_button.config(state=tk.DISABLED)
        status_label.config(text="Monitoring Started...", fg="green")
        
        simulate_health_monitoring(interval_seconds, duration_minutes)
        
        status_label.config(text="Monitoring Completed.", fg="blue")
        start_button.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Initialize the Tkinter window
root = tk.Tk()
root.title("Smart Healthcare Monitoring System")
root.geometry("600x400")
root.configure(bg="#2C3E50")  # Set background color to a dark shade for professional look

# Title Scrolling Label
title_frame = tk.Frame(root, bg="#34495E")
title_frame.pack(fill=tk.X, pady=10)
title_label = tk.Label(title_frame, text="Smart Healthcare Monitoring System", font=("Arial", 24, "bold"), fg="#ECF0F1", bg="#34495E")
title_label.pack(padx=20, pady=5)

scrolling_text = tk.Label(root, text="Welcome to Smart Healthcare Monitoring! Monitoring vitals for better health.", font=("Arial", 14, "italic"), fg="#ECF0F1", bg="#2C3E50")
scrolling_text.pack(fill=tk.X, padx=20, pady=10)

# Input Fields and Labels
input_frame = tk.Frame(root, bg="#2C3E50")
input_frame.pack(pady=10)

interval_label = tk.Label(input_frame, text="Interval (seconds):", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50")
interval_label.grid(row=0, column=0, padx=10, pady=5)

interval_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
interval_entry.grid(row=0, column=1, padx=10, pady=5)

duration_label = tk.Label(input_frame, text="Duration (minutes):", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50")
duration_label.grid(row=1, column=0, padx=10, pady=5)

duration_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
duration_entry.grid(row=1, column=1, padx=10, pady=5)

# Start Button
start_button = tk.Button(root, text="Start Monitoring", font=("Arial", 14, "bold"), fg="white", bg="#2980B9", command=start_monitoring)
start_button.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="Enter Interval and Duration to start.", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50")
status_label.pack(pady=5)

# Log Display
log_frame = tk.Frame(root, bg="#2C3E50")
log_frame.pack(pady=10, fill=tk.BOTH, expand=True)

log_text = tk.Text(log_frame, font=("Courier", 10), height=10, wrap=tk.WORD, bg="#34495E", fg="#ECF0F1", state=tk.DISABLED)
log_text.pack(fill=tk.BOTH, padx=20)

# Run the Tkinter main loop
root.mainloop()
