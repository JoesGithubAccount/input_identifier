import re

with open("test_data.txt", 'r') as f:
	test = f.read().splitlines()

#the chromosomal location format follows the format "number(s) letter numbers"
locus_search = re.compile(r'^\d{1,2}(Q|q|p|P)\d*.\d*')
	#don't want multiple p or q to be allowed, also don't want other letters allowed
#the Genbank accession number follows the format ""
#protein product name 
#gene identifier

for line in test:
	#print(line)
	thing = locus_search.search(line)
	if thing != None:
		print(thing, "chromosomal location")
	else:
		print("No match")