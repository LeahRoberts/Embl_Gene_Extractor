Extract genes from embl file
============================

A short python script to extract gene sequences from embl file(s).

To run the script:
------------------

	$ python extract_gene_from_embl.py <gene_name>

The script must be run above a directory called "genomes" containing all of the embl files that you wish to parse genes from. The gene name needs to exactly match that in the embl file (including case), eg: thrA, **not** THRA or thra. 

The script will iterate through all genomes and parse out all instances of the gene of interest. The script will create a "results" folder, which will contain all of the gene sequences. The header for each of these fasta files will contain the gene name, sequence start and end coordinates, as well as the genome that the gene came from. 

When there are more than one instance of the gene of interest, the files will be names <gene>.fna, <gene>_1.fna, <gene>_2.fna etc. 

NOTE: The script will not overwrite the "results" directory, however, if you run the script multiple times, the script may overwrite some of the .fna files in the results directory. 

Finding a number of genes:
-------------------------

The simplest way to do this is to create a list (list.txt) which contains all of the genes you wish to find. 

Then, using a simple loop, type:

	$ cat list.txt | while read $name; do python extract_gene_from_embl.py $name; done

As the gene names are different, nothing in the results folder should be overwritten. 



Parsing sequences from fasta files using coordinates
=====================================================

This script is designed to extract sequences from fasta files using coordinates given in a tab delimited file. 

File Setup:
------------

This script requires:

1. A tab-delimited file in this format:

	HVM2044_NODE_117_length_65041_cov_22.578804	CFT073_hly	99.00	7410	73	1	23077	30485	7410	1	0.0	13272  
	HVM2289_NODE_30_length_65039_cov_19.561985	CFT073_hly	99.00	7410	73	1	34629	42037	1	7410	0.0	13272
	HVM277_NODE_67_length_183966_cov_14.313231	CFT073_hly	99.01	7410	72	1	166552	173960	7410	1	0.0	13278
	HVM52_NODE_75_length_129723_cov_13.136999	CFT073_hly	99.00	7410	73	1	112332	119740	7410	1	0.0	13272

The first column will become the sequence header.
The second column name + ".fasta" will be the genome file used to parse the sequence from (which should be located in the "genome_files" directory - see below)
The 9th and 10th column should have the sequence coordinates - if the coordinates are for the reverse strand, the sequence will automatically be reverse complemented. 

2. A directory called "genome_files" containing all the fasta files from which the sequences will be parsed.

Script Usage:
-------------

The script should be executed above the "genome_files" directory:

	$ python parse_seq.py <tab-delimited-file-with-coordinates>

The output of the script will be a multi-fasta file called "outfile.fa".
