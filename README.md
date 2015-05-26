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


