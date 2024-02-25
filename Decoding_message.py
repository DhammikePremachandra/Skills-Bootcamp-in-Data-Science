def decode(message_file):
    """Extract the secret message hidden on the file and output it."""
    secret_message = extract_message(extract_data(message_file))
    print(f"Message:{secret_message}")

def extract_data(message_file):
    """Function to read the data on the file and return the 
     # dictionary.
    """
    data_dict = {}
    with open(message_file, "r", encoding='utf-8-sig') as file:
        """Open the file and create file object."""
        for line in file:
            # Check if there is a space in the line.
            if ' ' in line:
                # Split the line into key and value
                key, value = line.strip().split(' ')
                # Remove leading and trailing whitespace from the key 
                # and value.
                key = key.strip()
                value = value.strip()
                # Update the dictionary with the key-value pair.
                data_dict[key] = value
            else:
                # Outout Ignoring message if the line dosen't have a
                # delimiter.
                print(f"Ignoring line without delimiter: {line.strip()}")
    return data_dict

def extract_message(data_dict):
    """Function to exract the message(values of the dictionary) hidden 
       #on the file through keys of the dictionary. According to the 
       #base line of the pyramid,  always taken last number of the base 
       #line. Pyramid is an ordered by ascending."""
    t=0
    step = 1
    values_of_keys = ""
    while t < len(data_dict):
        t = t + step
        values_of_keys += data_dict[str(t)] + " "
        step += 1
    return values_of_keys.strip()

message_file = "coding_qual_input.txt"
decode(message_file)
