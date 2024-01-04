import os
import sys
from Bio import SeqIO

def parse_fasta_biopython(file_path):
    """
    Parse the fasta dataset into a dictionary format for efficient searching.
    
    Parameters:
    file_path (str): File path of the dataset
    
    Returns:
    fasta_dict (dict): The same dataset in the dictionary format
    
    """
    fasta_dict = {}
    for record in SeqIO.parse(file_path, "fasta"):
        id = record.id
        description = record.description
        sequence = str(record.seq)
        fasta_dict[id] = {'description': description, 'sequence': sequence}
    return fasta_dict

def write_fasta(id_file, output_file, seq_dict):
    """
    Writes a FASTA file from a dictionary of sequences.
    
    Parameters:
    id_file (str): Directory of the text file containing the list of IDs
    output_file (str): Directory of the output file to write to
    seq_dict (dict): Database in the dictionary format
    
    Returns:
    None
    """
    
    with open(id_file, 'r') as file:
        lines = file.readlines()
        
     # Check if file exists and is not empty
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        mode = 'a'  # Append mode
    else:
        mode = 'w'  # Write mode    
    
    for row in lines:
        id = row.strip()
        info_dict = seq_dict[id]
        
        with open(output_file, 'a') as file:
            file.write(f">{info_dict['description']}\n")
            file.write(f"{info_dict['sequence']}\n")
                        
if __name__ == "__main__":
    
    # Parse the dataset into a dictionary
    fasta_dict = parse_fasta_biopython('./uniprotkb_proteome_UP000005640_2023_10_05.fasta')
    
    # The systen argument will receive the machine index, e.g. the client machine has an index = 1
    id_file = f'./experiment_part_{sys.argv[1]}.txt'
    
    # Create the fasta file for model prediction
    write_fasta(id_file, f'./fasta_part_{sys.argv[1]}.fasta', fasta_dict)
