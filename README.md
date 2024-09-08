
# Ping with Progress Percentage

This Python script allows you to ping a specified host multiple times while displaying the progress percentage of the operation. The results of the ping operation are saved to a text file on your desktop for later review.

## Features

- Pings a specified host a given number of times.
- Displays a progress percentage indicating how many pings have been completed.
- Saves the raw output of the ping command to a text file on the desktop.

## Requirements

- Python 3.x
- No additional libraries are required, as the script uses built-in modules.

## Usage

1. **Run the Script**:
   Open a terminal or command prompt and execute the following command:

   ```bash
   python ping_logger.py
   ```

2. **Input Parameters**:
   - Enter the host you want to ping (e.g., `google.com`).
   - Enter the number of pings you want to send (e.g., `4`).

3. **View Results**:
   Once the pings are completed, check your desktop for a text file named `ping_output_<host>_<timestamp>.txt`, which contains the detailed results of the ping operation.

## Example

```bash
Enter the host to ping: google.com
Enter the number of pings: 4
Pinging...
Progress: 100.00%
Ping operation completed.
Output saved to /Users/yourusername/Desktop/ping_output_google.com_20240908_063000.txt
```

## Notes

- The progress percentage is displayed in real-time as the pings are processed.
- The output text file includes a timestamp and the number of pings requested.

## License
