import os
import json

class json_maker:

    # A summary json with data from a few sources
    # - couple tsv
    # - pdf variant list
    # - disease description (ClinVar/wiki/??)

    diseases_by_gene = {} 

    json_data = {'filename' : '',
            'focal_parent'  : '', 
            'affected_parent' : {}} # sublist is parents. Either, neither or both. 
                                    # sublist is genes (a person can have 0 or more). genes has a sublist of variants (a gene can have 1 or more). 
                                    # Variants have the details


    def parse_couple_tsv(self, tsv):
        with open(tsv, 'r') as t:
            header = t.readline().rstrip().split()
            lines = t.readlines()
            self.json_data['filename'] = tsv
            self.json_data['focal_parent'] = os.path.split(tsv)[1]

            for x in range(len(lines)):
                # parent ID
                parent_id = lines[x].split()[header.index('VCF_SAMPLE_ID')]

                if not parent_id in self.json_data['affected_parent']:
                    self.json_data['affected_parent'][parent_id] = {}

                # Try to lookup disease info by gene symbol
                gene_symbol = lines[x].rstrip().split()[0]
            
                disease_info = ['Unknown', 'Unknown']
                if gene_symbol in self.diseases_by_gene:
                    disease_info = self.diseases_by_gene[gene_symbol]

                # fill in gene data from TSV
                if gene_symbol not in self.json_data['affected_parent'][parent_id]:
                    self.json_data['affected_parent'][parent_id][gene_symbol] = {}
                    self.json_data['affected_parent'][parent_id][gene_symbol]['disease_desc'] = disease_info[1] 
                    self.json_data['affected_parent'][parent_id][gene_symbol]['diseases_name_(symbol)'] = disease_info[0] # pulled from symbol lookup 
                    self.json_data['affected_parent'][parent_id][gene_symbol]['variants'] = {}

                # fill in the variant data from the TSV (there is a lot more data in there. add fields as needed)
                variant_col = header.index('AAChange.refGene')
                variant = lines[x].split('\t')[variant_col]
                if variant not in self.json_data['affected_parent'][parent_id][gene_symbol]['variants']:
                    self.json_data['affected_parent'][parent_id][gene_symbol]['variants'][variant] = {}
                    self.json_data['affected_parent'][parent_id][gene_symbol]['variants'][variant]['disease_name_(CLNDN)'] = lines[x].split('\t')[header.index('CLNDN')] 
                    self.json_data['affected_parent'][parent_id][gene_symbol]['variants'][variant]['inheritance'] = lines[x].rstrip().split('\t')[header.index('X3')] 

       
    def parse_variant_list(self, variant_list):
        # populate the   global directory with gene info

        with open(variant_list, 'r') as t:
            for g in t:
                gene_symbol = g.rstrip().split()[0]
                self.diseases_by_gene[gene_symbol] = g.rstrip().split('\t')


    #FIXME
    '''
    def add_disease_defs(self, #FIXME)
    '''

if __name__ == '__main__':

    tsv_files = ['2019100110022_ann_panel.tsv']
    for i in range(len(tsv_files)):
            jm = json_maker()
            jm.parse_variant_list('/home/nathan/variant_tst_to_json/data/23-25-trio-clinical-report-fields.txt')
            jm.parse_couple_tsv('/home/nathan/variant_tst_to_json/data/tsv/2019100110022_ann_panel.tsv')

            print(str(jm.json_data))
            print(json.loads('"' + str(jm.json_data)) + '}"')

