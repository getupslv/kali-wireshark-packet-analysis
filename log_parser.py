# log_parser.py
# A simple script to find unencrypted web traffic in a network log file.

def scan_log(file_name):
    print(f"--- Scanning {file_name} for Insecure HTTP Traffic ---")
    insecure_count = 0
    
    try:
        with open(file_name, 'r') as file:
            for line_num, line in enumerate(file, 1):
                # Search for unencrypted http:// traffic
                if "http://" in line.lower():
                    print(f"[ALERT] Line {line_num}: Found unencrypted HTTP traffic -> {line.strip()}")
                    insecure_count += 1
                    
        print("\n--- Scan Complete ---")
        print(f"Total insecure protocols detected: {insecure_count}")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please create it first.")

# Run the parser on a sample log file
scan_log("network_log.txt")
