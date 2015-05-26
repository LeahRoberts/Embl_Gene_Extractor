#!/usr/bin/env python

import glob
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation
import sys
import os, errno

def mkdir(path, overwrite=False):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            if not overwrite:
                print "path '%s' already exists" % path   # overwrite == False and we've hit a directory that exists
        else: raise


in_files = glob.glob('genomes/*.embl')

mkdir('results')

stored = {}

for f in in_files:

        cur_genome = SeqIO.parse(f, "embl")
        for record in cur_genome:
            for feat in record.features:
                    if feat.type == 'CDS':
                        if 'gene' in feat.qualifiers:
                            gene = feat.qualifiers['gene'][0]
                            if gene == sys.argv[1]:
                                s, e, strand = feat.location.start, feat.location.end, feat.location.strand
                                header = '>'+feat.qualifiers['gene'][0]+","+str(s+1)+".."+str(e)+"("+str(strand)+")"+","+"["+f.replace("genomes/", "")+"]"
                                flanked = FeatureLocation(s, e, strand)
                                out_seq = flanked.extract(record.seq)
                                fname = header[1:].split(',')[0]+".fna"

                                if fname in stored.keys():
                                    old = fname
                                    fname = fname.replace(".fna", "_"+str(stored[fname])+".fna")
                                    stored[old] = stored[old]+1
                                else:
                                    stored[fname] = 1

                                with open(os.path.join('results', fname), 'w') as out:
                                    out.write(header+'\n')
                                    out.write(str(out_seq)+'\n')
