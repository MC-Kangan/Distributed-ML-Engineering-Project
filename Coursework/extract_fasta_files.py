import os
import sys
from Bio import SeqIO


def parse_fasta_biopython(file_path):
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

    :param filename: Name of the file to write to.
    :param seq_dict: Dictionary where keys are sequence identifiers and values are sequences.
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
    
    # Parse all the fasta dict
    fasta_dict = parse_fasta_biopython('./uniprotkb_proteome_UP000005640_2023_10_05.fasta')
    
    id_file = f'./experiment_part_{sys.argv[1]}.txt'
    
    # Create the fasta file for model prediction
    write_fasta(id_file, f'./fasta_part_{sys.argv[1]}.fasta', fasta_dict)
