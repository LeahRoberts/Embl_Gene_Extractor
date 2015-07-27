#!/user/bin/env python

# Script for parsing sequences using a tab delimited file

# Setup:
# Make a directory called "genome_files" and put all of the reference fasta file in this folder.
# This folder and the fasta file inside will be used to parse the sequences from.
# Execute the script ABOVE the "genome_files" directory.
# Have a tab-delimited file with:
#   - The header name as the first column
#   - The reference genome as the second column
#   - The coordinates as the 9th and 10th columns
# Sequences on the reverse strand will automatically be reverse complemented in the final "outfile.fasta" file.

# Script execution:
# $ python parse_seq.py <tab-file-with-locations>

import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

in_file = sys.argv[1]
genome_path = os.path.abspath("genome_files/")

with open(in_file) as f:
    content = f.readlines()
    for line in content:
        source = os.path.join(genome_path, line.split("\t")[1] + ".fasta")
        header = ">" + line.split("\t")[0] + "_" + source.split(".")[0]
        seq_start = int(line.split("\t")[8]) - 1
        seq_end = int(line.split("\t")[9]) + 1
        if seq_start > seq_end:
            seq_start = int(line.split("\t")[9]) - 1
            seq_end = int(line.split("\t")[8]) + 1

            for line in SeqIO.parse(source, "fasta"):
                out_seq = line.seq[seq_start:seq_end]
                final_seq = str(out_seq.reverse_complement())
                with open("outfile.fa", "a") as out:
                    out.write(header + "\n")
                    out.write(final_seq + "\n")

        else:
            for line in SeqIO.parse(source, "fasta"):
                out_seq = str(line.seq[seq_start:seq_end])
                with open("outfile.fa", "a") as out:
                    out.write(header + "\n")
                    out.write(out_seq + "\n")
