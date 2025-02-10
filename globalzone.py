import os
import time
import psutil
import GPUtil
from plyer import notification

# Define thresholds for CPU and GPU temperatures
CPU_TEMP_THRESHOLD = 80  # Celsius
GPU_TEMP_THRESHOLD = 85  # Celsius

def get_cpu_temperature():
    # Function to get CPU temperature
    temp_sensors = psutil.sensors_temperatures()
    if 'coretemp' in temp_sensors:
        for entry in temp_sensors['coretemp']:
            if entry.label.startswith("Package id"):
                return entry.current
    return None

def get_gpu_temperature():
    # Function to get GPU temperature
    gpus = GPUtil.getGPUs()
    if gpus:
        return gpus[0].temperature
    return None

def check_temperatures():
    cpu_temp = get_cpu_temperature()
    gpu_temp = get_gpu_temperature()

    if cpu_temp and cpu_temp >= CPU_TEMP_THRESHOLD:
        notification.notify(
            title="Overheating Alert!",
            message=f"CPU Temperature is too high: {cpu_temp}°C",
            timeout=5
        )
    
    if gpu_temp and gpu_temp >= GPU_TEMP_THRESHOLD:
        notification.notify(
            title="Overheating Alert!",
            message=f"GPU Temperature is too high: {gpu_temp}°C",
            timeout=5
        )

def main():
    while True:
        check_temperatures()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()