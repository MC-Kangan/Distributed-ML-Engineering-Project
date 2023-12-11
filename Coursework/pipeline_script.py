import sys
from subprocess import Popen, PIPE
from Bio import SeqIO
from prometheus_client import start_http_server, Gauge

# Create a gauge metric
progress_percent_metric = Gauge('ML_prediction_progress_percentage', 'Progress of ML predictions (%)')
progress_count_metric = Gauge('ML_prediction_progress_count', 'Progress of ML predictions (count)')

"""
usage: python pipeline_script.py INPUT.fasta  
approx 5min per analysis
"""

def run_parser(hhr_file):
    """
    Run the results_parser.py over the hhr file to produce the output summary
    """
    cmd = ['python', './results_parser.py', hhr_file]
    print(f'STEP 4: RUNNING PARSER: {" ".join(cmd)}')
    p = Popen(cmd, stdin=PIPE,stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out.decode("utf-8"))

def run_hhsearch(a3m_file, machine_id):
    """
    Run HHSearch to produce the hhr file
    """
    if machine_id == '1':
        num_thread = 4 - 1
    else:
        num_thread = 2 - 1
        
    cmd = ['/home/ec2-user/data/hh_suite/bin/hhsearch',
           '-i', a3m_file, '-cpu', num_thread, '-d', 
           '/home/ec2-user/data/pdb70/pdb70']
    print(f'STEP 3: RUNNING HHSEARCH: {" ".join(cmd)}')
    p = Popen(cmd, stdin=PIPE,stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    

def read_horiz(tmp_file, horiz_file, a3m_file):
    """
    Parse horiz file and concatenate the information to a new tmp a3m file
    """
    pred = ''
    conf = ''
    print("STEP 2: REWRITING INPUT FILE TO A3M")
    with open(horiz_file) as fh_in:
        for line in fh_in:
            if line.startswith('Conf: '):
                conf += line[6:].rstrip()
            if line.startswith('Pred: '):
                pred += line[6:].rstrip()
    with open(tmp_file) as fh_in:
        contents = fh_in.read()
    with open(a3m_file, "w") as fh_out:
        fh_out.write(f">ss_pred\n{pred}\n>ss_conf\n{conf}\n")
        fh_out.write(contents)

def run_s4pred(input_file, out_file, machine_id):
    """
    Runs the s4pred secondary structure predictor to produce the horiz file
    """
    
    if machine_id == '1':
        num_thread = 4 - 1
    else:
        num_thread = 2 - 1
    
    cmd = ['/usr/bin/python3', '/home/ec2-user/data/s4pred/run_model.py',
           '-t', 'horiz', '-T', num_thread, input_file]
    print(f'STEP 1: RUNNING S4PRED: {" ".join(cmd)}')
    p = Popen(cmd, stdin=PIPE,stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    with open(out_file, "w") as fh_out:
        fh_out.write(out.decode("utf-8"))

    
def read_input(file):
    """
    Function reads a fasta formatted file of protein sequences
    """
    print("READING FASTA FILES")
    sequences = {}
    ids = []
    for record in SeqIO.parse(file, "fasta"):
        sequences[record.id] = record.seq
        ids.append(record.id)
    return(sequences)

if __name__ == "__main__":
    
    machine_id = str(sys.argv[1])
    test = sys.argv[2] # If test == T means testing mode, else non-testing mode
    
    start_http_server(8000)
    
    if test == 'T':
        sequences = read_input(f'test.fa')
    else:
        sequences = read_input(f'fasta_part_{machine_id}.fasta')
    
    tmp_file = "tmp.fas"
    horiz_file = "tmp.horiz"
    a3m_file = "tmp.a3m"
    hhr_file = "tmp.hhr"
    counter = 0
    for k, v in sequences.items():
        with open(tmp_file, "w") as fh_out:
            fh_out.write(f">{k}\n")
            fh_out.write(f"{v}\n")
        
        run_s4pred(tmp_file, horiz_file, machine_id)
        read_horiz(tmp_file, horiz_file, a3m_file)
        run_hhsearch(a3m_file, machine_id)
        run_parser(hhr_file)
        counter += 1
        progress_percent_metric.set((counter + 1) / len(sequences) * 100)
        progress_count_metric.set(counter)
