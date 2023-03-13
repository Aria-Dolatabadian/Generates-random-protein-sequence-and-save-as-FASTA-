from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO

import random

# Define the length of the sequence
seq_length = 5000

# Define the amino acids to choose from
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Generate the random sequence
seq = "".join([random.choice(amino_acids) for _ in range(seq_length)])

# Create a Seq object with the sequence
seq_obj = Seq(seq, Seq)

# Create a SeqRecord object with the sequence
seq_record = SeqRecord(seq_obj)

# Add metadata to the sequence record
seq_record.id = "RandomProtein"
seq_record.description = "A random protein sequence"

# Write the sequence record to a FASTA file
with open("output.fasta", "w") as output_handle:
    SeqIO.write(seq_record, output_handle, "fasta")
