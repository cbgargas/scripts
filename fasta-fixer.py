#! /usr/bin/python

import argparse
from Bio import SeqIO

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'imports and corrects shitty fasta files')

#adding positional arguments to parser
parser.add_argument('infile', help='.fasta file you wish to parse by .gff features', type=str)
parser.add_argument('-o','--outfile', help='name for your output file', type=str, default='output.fa')

#parse the cmd line arguments
args = parser.parse_args()

#open your output file for writing
with open(args.outfile, 'w') as output:
    #open your input fasta file
    with open(args.infile) as fasta:
        #read in fasta file with SeqIO
        fsa = SeqIO.parse(fasta, 'fasta')

        #gives available options for an object
        print(dir(fsa))


        #add an if/then statement for sequence headers
#        for line in fsa:
#            if line.find('>'):
#                line.replace(' ', '_')
#                line.replace('\t', '_')
#                outfile.write(line)
#            else:
#                line.replace(' ', '')
#                output.write(line)

#        out = SeqIO.write(fsa, output, 'fasta-2line')






#close the files 		
output.close()
fasta.close()

