#! /usr/bin/python

import os
import argparse
from Bio import SeqIO

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'Imports and corrects shitty fasta files (e.g., Silva LTP fasta files).')

#adding positional arguments to parser
parser.add_argument('infile', help='phylogenetics file you want to reformat', type=str)

#adding optional arguments to parser
parser.add_argument('-f1','--format1', help='format of input file', type=str, default='fasta')
parser.add_argument('-f2','--format2', help='format for output file', type=str, default='fasta-2line')
parser.add_argument('-o','--outfile', help='name for your output file', type=str, default='output.fa')

#parse the cmd line arguments
args = parser.parse_args()



#open your output file for writing
with open('intermediate1.fa', 'w') as intermediate1:
    #open your input fasta file
    with open(args.infile) as fasta: 
        #read in fasta file with SeqIO
        SeqIO.convert(fasta, args.format1, intermediate1, args.format2)
        #gives available options for an object
        #print(dir(fsa))
        with open('intermediate2.fa', 'w') as intermediate3:
            #open your output1 file for writing
            with open('intermediate1.fa', 'r') as intermediate2:
            #add an if/then statement for sequence headers
                for line in intermediate2:
                    if line.find('>'):
                        intermediate3.write(line.replace('.', '-'))
                    else:
                        intermediate3.write(line.replace(' ', '_'))
                with open(args.outfile, 'w') as output:   
                    with open('intermediate2.fa', 'r') as intermediate4:
                        for line in intermediate4:
                            if line.find('\t'):
                                output.write(line.replace('\t', '_'))
                            else:
                                continue
#cremove intermediate files
os.remove('intermediate1.fa')
os.remove('intermediate2.fa') 

