import sys

with open(sys.argv[1],'r') as gene_list:
    for g in gene_list:
        elts = g.rstrip().split(". ")
        syndrome_symbol  = elts[0]
        inheritence = 'NULL'
        
        ss_elts = syndrome_symbol.split(" - ")

        #print(ss_elts)
        symbol = ss_elts[1][6:]
        syndrome = ss_elts[0]
        if len(elts) > 1:
            inheritence = elts[1]

        print(f'{symbol}\t{syndrome}\t{inheritence}')
