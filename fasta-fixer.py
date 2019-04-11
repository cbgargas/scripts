#! /usr/bin/python

import argparse
from Bio import SeqIO

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'Imports and corrects shitty fasta files (e.g., Silva LTP fasta files).')

#adding positional arguments to parser
parser.add_argument('infile', help='.fasta file you wish to parse by .gff features', type=str)

#adding optional arguments to parser
parser.add_argument('-f1','--format1', help='format of input file', type=str, default='fasta')
parser.add_argument('-f2','--format2', help='desired output format for output file', type=str, default='fasta-2line')
parser.add_argument('-o','--outfile', help='name for your output file', type=str, default='output.fa')

#parse the cmd line arguments
args = parser.parse_args()

#open your output file for writing
with open('output1.fa', 'w') as output1:
    #open your input fasta file
    with open(args.infile) as fasta: 
        #read in fasta file with SeqIO
        fsa = SeqIO.convert(fasta, args.format1, output1, args.format2)
        #gives available options for an object
        #print(dir(fsa))
        with open(args.outfile, 'w') as output2:
            #open your output1 file for writing
            with open('output1.fa', 'r') as fasta2:
            #add an if/then statement for sequence headers
                for line in fasta2:
                    if line.find('>'):
                        output2.write(line.replace('.', '-'))
                    else:
                        output2.write(line.replace('\t'or' ', '_'))



#close the files 	
output1.close()
fasta.close()
output2.close()
fasta2.close()

