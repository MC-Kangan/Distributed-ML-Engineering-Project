import os

def split_file_into_parts(filename, num_parts):
    """
    Splits the file specified by filename into num_parts equal parts.
    Each part will be saved as a separate file.
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
        with open(f'experiment_part_{i+1}.txt', 'w') as part_file:
            part_file.writelines(part)
            
            
if __name__ == "__main__":
    split_file_into_parts('./experiment_ids.txt', 5)