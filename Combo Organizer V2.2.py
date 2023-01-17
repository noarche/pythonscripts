import os
import threading

# Open the input file
with open('input.txt', 'r') as f:
    # Read all the lines in the file
    lines = f.readlines()

# Initialize a dictionary to store the lines for each domain
domain_lines = {}

# Create a lock to protect access to the dictionary
lock = threading.Lock()

def process_line(line):
    # Check if the line contains an @ symbol
    if '@' in line:
        # Extract the domain from the line
        domain = line[line.index('@')+1:line.index('.')]
        
        # Acquire the lock
        lock.acquire()
        
        # Initialize an empty list for the domain if it doesn't already exist
        if domain not in domain_lines:
            domain_lines[domain] = []
        
        # Add the line to the list for the domain
        domain_lines[domain].append(line)
        
        # Release the lock
        lock.release()

# Create a thread for each line in the file
threads = []
for line in lines:
    t = threading.Thread(target=process_line, args=(line,))
    threads.append(t)

# Start all the threads
for t in threads:
    t.start()

# Wait for all the threads to finish
for t in threads:
    t.join()

# Create a text file for each domain
for domain, lines in domain_lines.items():
    # Create the file name for the domain
    file_name = f'{domain}.txt'
    
    # Open the file for writing
    with open(file_name, 'w') as f:
        # Write the lines to the file
        f.writelines(lines)
        
# Let the user know that we are done
print("SUCCESSFULLY COMPLETED ORGANIZATION!")