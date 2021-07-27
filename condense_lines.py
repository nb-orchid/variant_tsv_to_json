import sys

with open(sys.argv[1], 'r') as gene_list, open(sys.argv[2], 'w') as out_file:
    curr_line = []
    for g in gene_list:
        if not "Gene: " in g:
            curr_line.append(g.rstrip())
        else:
            print(g.rstrip() + " " + " ".join(curr_line), file = out_file)
            curr_line = []

