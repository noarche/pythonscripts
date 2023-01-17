import os

# Open the file "mkDir.txt" and read its contents into a list
with open("mkDir.txt", 'r') as f:
    lines = f.readlines()

# Iterate over the list of lines
for line in lines:
    # Strip leading and trailing whitespace from the line
    line = line.strip()

    # Create a new directory with the name of the line
    os.mkdir(line)

# Let the user know that we are done
print("Done!")
