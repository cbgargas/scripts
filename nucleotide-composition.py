#!/usr/bin/python3

#This script calculates and reports nucleotide composition for a DNA seqeunces

#get a DNA sequence - we'll make on up for now

dna_seq = 'AAACTTGGGTACGATCAGCTACGAAATTTCCCATCACTACTACTAGGGG'
#how would we correct for a seqeunce that contained spaces or none gene code info?
#dna_seq = ' AAACTTGGGTACGATCAGCTACGAAATTTCCCATCACTACTACTAGGGG '


#if sequence is masked like so:
#dna_seq = 'AAAcccTTTGGG'
#then the C's won't register, so we need to convert all characters in the string to uppercase
#dna_seq = dna_seq.upper()

#print(dna-seq)

#calculate the sequence length

sequence_length = len(dna_seq)
print('sequence length:',(sequence_length))

#prints w/o space, need to add str() to make the integer into a string
print('sequence length:' + str(sequence_length))


#Calculate number of A, C, G, T

numA = dna_seq.count('A')
numC = dna_seq.count('C')
numG = dna_seq.count('G')
numT = dna_seq.count('T')

#calulates freq of A,C,G,T
freqA = ((numA/sequence_length)*100)
freqC = ((numC/sequence_length)*100)
freqG = ((numG/sequence_length)*100)
freqT = ((numT/sequence_length)*100)

#print the output
print('freq of A: %.2f' % freqA)
print('freq of C: %.2f' % freqC)
print('freq of G: %.2f' % freqG)
print('freq of T: %.2f' % freqT)

#checking that our freqs add up
#print(freqA + freqC + freqG + freqT)

