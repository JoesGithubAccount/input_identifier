import re

with open("test_data.txt", 'r') as f:
	test = f.read().splitlines()

#the chromosomal location format follows the format "number(s) letter numbers"
locus_search = re.compile(r'^\d{1,2}(Q|q|p|P)\d*.\d*')
#the Genbank accession number follows the format "letter5number/2letter6number(nucleotide) 3letter5number(protein)"
acc_search = re.compile(r'^')
#gene identifier seems to be 4 characters starting with letters
gi_search = re.compile(r'^')
#protein product name follows much looser characteristics "else"
ppn_search = re.compile(r'^')

for line in test:
	#print(line)
	thing = locus_search.search(line)
	if thing != None:
		print(thing, "chromosomal location")
	else:
		print("No match")