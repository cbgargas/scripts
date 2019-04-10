#! /usr/bin/python 

import csv 

#open the output file
with open('shaver_etal.tab', 'w') as tabout:

#open the data file
    with open('example_files/shaver_etal.csv', 'r') as shaver:
        #create a csv reader object    
        csvreader = csv.reader(shaver, delimiter=',')

        for line in csvreader:
            if not line:
                continue
            else:
                #print(line[0], line[5])
                
                #create a csv writer object
                linewriter = csv.writer(tabout, delimiter='\t', quotechar = '"')
                linewriter.writerow(line) 

    #for line in shaver:
    #print(line)









