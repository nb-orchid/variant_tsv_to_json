import json

class json_maker

    # A summary json with data from a few sources
    # - couple tsv
    # - pdf variant list
    # - disease description (ClinVar/wiki/??)

    disease_by_gene = {} 

    json_data = {"filename" : ''
            "focal_parent", 
            "affected_parent" : []} # sublist is parents. Either, neither or both. 
                                    # sublist is genes (a person can have 0 or more). genes has a sublist of variants (a gene can have 1 or more). 
                                    # Variants have the details


    def parse_couple_tsv(self, tsv):
        with t as open (tsv, 'r'):
            header = t.readline.rstrip().split()
            lines = t.readlines()
            self.json_data['filename' : tsv]
            self.json.data['focal_parent'] = tsv[:10]

            for x in lines[1:]
                # parent ID
                c = header.index("VCF_SAMPLE_ID")
                parent_id = header[x]

                if not parent_id in json_data['affected_parent']
                    json_data['affected_parent'][parent_id] == {}

                # Try to lookup disease info by gene symbol
                gene_symbol = x[0]
            
                disease_info = ["Unknown", "Unknown"]
                if gene_symbol in disease_by_gene:
                    disease_info = disease_by_gene[gene_symbol]

                # fill in gene data from TSV
                if gene_symbol not in json_data['affected_parent'][parent_id]:
                    self.json_data['affected_parent'][parent_id][gene_symbol] = {}
                        ['affected_parent'][parent_id][gene_symbol]["disease_desc"] = dieases_info[0]
                        ['affected_parent'][parent_id][gene_symbol]["diseases_name"] = disease_info[1]
                        ['affected_parent'][parent_id][gene_symbol]['variants'] = {}

                # fill  in the variant data from the TSV (there is a lot more data in there. add fields as needed)
                variant_col = t.index("AAChange.refGene")
                variant = x[variant_col]
                if variant not in ['affected_parent'][parent_id][gene_symbol]['variants']:
                    ['affected_parent'][parent_id][gene_symbol]['variants'][variant] = {}
                    ['affected_parent'][parent_id][gene_symbol]['variants'][variant]['disease_name'] = x[t.index['CLNDN'] 
                    ['affected_parent'][parent_id][gene_symbol]['variants'][variant]['inheritance'] = x[t.index['X3'] 

       
    def parse_variant_list(self, variant_list):
        # populate the   global directory with gene info

        with t as open(tsv, 'r')
            for g in t:
                gene_symbol = rstrip().split()g[0]
                self.diseases_by_gene[gene_symbol] = g.rstrip().split()



    """
    def add_disease_defs(self, #FIXME)
    """


if __name__ == "__main__":

    tsv_files = ['2019100110022_ann_panel.tsv']
    for tsv in tsv_files:
        with open(f'/home/variant_tst_to_json/data/{tsv_files[0]}' as tsv, 
             open("/home/data/data/23-25-trio-clinical-report-fields.txt", 'r') as clin:

            jm = json_maker()
            jm.parse_variant_list(clin)
            jm.parse_couple_tsv(tsv)

            print(jm.json_data)





