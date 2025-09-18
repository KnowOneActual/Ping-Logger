import os
import platform
import subprocess
import datetime
import re

def get_desktop_path():
    """Gets the user's desktop path."""
    return os.path.join(os.path.expanduser("~"), "Desktop")

def save_output_to_file(output, host, count):
    """Saves the ping output to a text file on the desktop."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ping_output_{host}_{timestamp}.txt"
    desktop_path = os.path.join(get_desktop_path(), filename)
    
    with open(desktop_path, 'w') as file:
        file.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Ping results for {host}:\n")
        file.write(f"Number of pings: {count}\n\n")
        file.write(output)
    
    print(f"\nOutput saved to {desktop_path}")

def ping_host_with_progress(host, count):
    """Pings the host and displays real-time progress."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    print(f"Pinging {host} {count} times...")
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    full_output = []
    pings_completed = 0
    
    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break
        if output:
            full_output.append(output)
            # This regex is a simple way to check for a successful ping reply.
            # It might need to be adjusted for different languages or ping versions.
            if "Reply from" in output or "bytes from" in output:
                pings_completed += 1
                progress = (pings_completed / count) * 100
                print(f"\rProgress: {progress:.2f}%", end="")

    # Capture any remaining output and errors
    stdout, stderr = process.communicate()
    full_output.append(stdout)
    if stderr:
        full_output.append(stderr)

    return "".join(full_output)

def main():
    """Main function to run the ping logger."""
    host = input("Enter the host to ping: ")
    while True:
        try:
            count_str = input("Enter the number of pings: ")
            count = int(count_str)
            if count > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    output = ping_host_with_progress(host, count)
    
    if output:
        print("\nPing operation completed.")
        save_output_to_file(output, host, count)
    else:
        print("\nCould not get ping output.")

if __name__ == "__main__":
    main()