#! /usr/bin/python 

#import argument parser and seqio from biopython(Bio)
import argparse
from Bio import SeqIO

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'extracts sequences from a genome based on features in a .gff file')

#adding positional arguments to parser
parser.add_argument('fasta_file', help='.fasta file you wish to parse by .gff features', type=str)
parser.add_argument('gff_file', help='.gff file that you will use to parse your .fasta genome file', type=str)

#parse the cmd line arguments
args = parser.parse_args()

#biopython method for parsing fasta files:
fasta_file = SeqIO.parse(open(args.fasta_file),'fasta')
with open(output_file) as out_file:
    for seq in fasta_file:
        name, seq = fasta.id, str(fasta.seq)
        #new_sequence = some_function(sequence)
        #write_fasta(out_file)
		print(seq)


# your solution to open the fasta file, via .split()
#fasta = open(args.fasta_file, "r")
#genome=fasta.read().rstrip('\n')
#header,seq= genome.split('\n')
#print(seq)

#alternative way to do .split()
#fasta_contents =args.fasta_file.read()
#header= args.fasta_file.split('\n')[0]
#seq== args.fasta_file.split('\n')[1]
#fasta_file.close()

#solution 2, using next():
#sequence=next(args.fasta_file)
#sequence=args.fasta_file.read()
#seqeuence = seqeunce.rstrip(\n)

#solution 3, for loop:
#line_counter=1
#for line in args.fasta_file:
#	if line_counter ==2:
#		sequence == line.rstrip('\n')
#	line_counter += 1

#solution 4, with statement
#file_in_list=[]
#with open(args.fasta_file) as args.fasta_file:
#	file_in_list = args.fasta_file.read().splitlines()
#	file_in_list = args.fasta_file.splitlines()
#	genome = file_in_list[1]


# open the gff file
gff=open(args.gff_file, "r")

#print header info
print(header)

# read the gff file line by line
for line in gff:

	#removing line breaks
	line = line.rstrip('\n')
	#print(line)
	#split each line on the tab character
	sequence, source, feature, start, end, length, strand, phase, attributes = line.split('\t')

	#print(start, end)
	#print(start_n, end_n)

#extract the DNA seq from the genome
	#define feature coordinates for python
	start_n=int(start)-1
	end_n=int(end)+1
	
	#create substring to pull feeature from
	substring=seq[start_n:end_n]
	
	#print feature coordinates
	print(start+':'+end)
	
	#print the DNA seq of this feature
	print(substring)

# calculate the GC content for this feature
	#calculates length of substring
	sequence_length = len(substring)

#calculates number of respective nucleotide in substring
	#numA = substring.count('A')
	numC = substring.count('C')
	numG = substring.count('G')
	#numT = substring.count('T')

#calulates freq of A,C,G,T
	#freqA = ((numA/sequence_length)*100)
	freqC = ((numC/sequence_length)*100)
	freqG = ((numG/sequence_length)*100)
	#freqT = ((numT/sequence_length)*100)

#print the output
	#print('freq of A: %.2f' % freqA)
	print('freq of G: %.2f,' % freqG, 'freq of C: %.2f' % freqC)
	#print('freq of T: %.2f' % freqT)
	
#close the files 		
gff.close()
fasta.close()