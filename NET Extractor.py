# Open the input file in read mode
with open('combo.txt', 'r') as f:
  # Open the output file in write mode
  with open('NET_extracted.txt', 'w') as out:
    # Iterate over the lines in the input file
    for line in f:
      # Check if the line contains the string ".net"
      if ".net" in line:
        # Write the line to the output file
        out.write(line)