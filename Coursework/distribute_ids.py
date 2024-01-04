import os


def split_file_into_parts(filename, num_parts):
    """
    Splits the file specified by filename into num_parts equal parts.
    Each part will be saved as a separate file.
    
    Parameters:
       filename (str): Filename to be read and split into parts
       num_parts (int): Number of parts to split the file into
       
    Returns:
       None
    """
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Calculate the number of lines per part
    total_lines = len(lines)
    lines_per_part = total_lines // num_parts

    # Split the lines into parts
    parts = []
    for i in range(num_parts):
        start_index = i * lines_per_part
        end_index = start_index + lines_per_part
        parts.append(lines[start_index:end_index])

    # Save each part to a separate file
    for i, part in enumerate(parts):
        
        # When index = 0 or 1, allocate both parts to experiment_part_1.txt, 
        # which is allocated to the client machine
        
        if i == 0:
            with open(f'experiment_part_1.txt', 'w') as part_file:
                part_file.writelines(part)
        elif i == 1:
            with open(f'experiment_part_1.txt', 'a') as part_file:
                part_file.writelines(part)
        else:
            with open(f'experiment_part_{i}.txt', 'w') as part_file:
                part_file.writelines(part)
            

if __name__ == "__main__":
    # Split the file into 6 parts (1000 ids per part)
    # Client machine has more cpus thus takes 2 parts (2000 ids), which is stored in experiment_part_1
    # Cluster mchines have less cpus thus take 1 part (1000 ids) each, which are stored in experiment_part_2 to 5 
    split_file_into_parts('./experiment_ids.txt', 6)
    
    
    