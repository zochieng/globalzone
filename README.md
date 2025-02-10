# GlobalZone

GlobalZone is a Python-based monitoring tool designed to keep an eye on CPU and GPU temperatures on Windows systems. It provides alerts if either the CPU or GPU temperatures exceed predefined thresholds, helping to prevent overheating and potential damage to your hardware.

## Features

- Monitors CPU temperature
- Monitors GPU temperature
- Sends desktop notifications when temperatures exceed safe thresholds

## Requirements

- Python 3.x
- `psutil` library for accessing system sensors
- `GPUtil` library for accessing GPU information
- `plyer` library for sending desktop notifications

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/globalzone.git
```

2. Install the required libraries:

```bash
pip install psutil GPUtil plyer
```

## Usage

Run the `globalzone.py` script to start monitoring:

```bash
python globalzone.py
```

The program will check the CPU and GPU temperatures every 60 seconds and alert you if they exceed the set thresholds.

## Configuration

You can adjust the temperature thresholds by modifying the `CPU_TEMP_THRESHOLD` and `GPU_TEMP_THRESHOLD` variables in `globalzone.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.