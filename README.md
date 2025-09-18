# Ping Logger with Real-Time Progress

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)

This Python script lets you ping a host multiple times and see the progress in real-time. It works on Windows, macOS, and Linux, and it saves the full ping output to a text file on your desktop.


## Features



* Pings a host a specific number of times.
* Displays a real-time progress bar.
* Saves the detailed ping results to a text file.
* Cross-platform: Works on Windows, macOS, and Linux.


## Requirements



* Python 3.x


## How to Use



1. **Run the script from your terminal:** 
```bash
python ping_logger.py 
```


2. **Enter the host you want to ping** (e.g., google.com).
3. **Enter how many times you want to ping** (e.g., 10).

The script will start pinging and show you the progress. Once it's done, you'll find a text file named ping_output_&lt;host>_&lt;timestamp>.txt on your desktop with the results.


## Example

Enter the host to ping: google.com 
Enter the number of pings: 4 
Pinging google.com 4 times... 
Progress: 100.00% 
Ping operation completed. 
 
Output saved to /Users/yourusername/Desktop/ping_output_google.com_20250918_143800.txt 



## License

This project is licensed under the MIT License.