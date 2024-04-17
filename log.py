# Import the read_file function from the module
from read_file import read_file

# Define a function to analyze log entries
def analyze_log(log_file):
    # Read the contents of the log file
    log_contents = read_file(log_file)

    # Process each log entry
    for log_entry in log_contents.split('\n'):
        # Extract useful information from each log entry
        if 'ERROR' in log_entry:
            print("Error found:", log_entry)
        elif 'WARNING' in log_entry:
            print("Warning found:", log_entry)
        # Add more conditions for other types of log entries (e.g., INFO, DEBUG)

# Example usage:
analyze_log("app.log")
