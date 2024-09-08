import os
import platform
import subprocess
import datetime
import time

def ping_host(host, count):
    # Determine the command based on the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    print("Pinging...")
    
    # Execute the ping command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    
    return result.stdout

def save_output_to_file(output, host, count):
    # Create a filename with the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ping_output_{host}_{timestamp}.txt"
    
    # Define the path for Windows and Unix-based systems
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", filename)
    
    # Write the output to the file
    with open(desktop_path, 'w') as file:
        file.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Ping results for {host}:\n")
        file.write(f"Number of pings: {count}\n\n")
        file.write(output)
    
    print(f"Output saved to {desktop_path}")

def main():
    host = input("Enter the host to ping: ")
    count = int(input("Enter the number of pings: "))
    
    # Start the ping operation and measure progress
    print("Pinging...")
    output = ping_host(host, count)
    
    # Simulate a progress display
    for i in range(count):
        # Calculate and display the percentage completed
        percent_complete = (i + 1) / count * 100
        print(f"\rProgress: {percent_complete:.2f}%", end="")
        time.sleep(1)  # Simulate the time taken for each ping; adjust as necessary

    print("\nPing operation completed.")
    
    # Save the output to a file
    save_output_to_file(output, host, count)

if __name__ == "__main__":
    main()
