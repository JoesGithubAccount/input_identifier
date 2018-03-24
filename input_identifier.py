import re

with open("test_data.txt", 'r') as f:
	test = f.read().splitlines()

#the chromosomal location format follows the format "number(s) letter numbers"
loc_search = re.compile(r'^\d{1,2}(Q|q|p|P)\d*.\d*$')
#the Genbank accession number follows the format "letter5number/2letter6number" for old and new respectively
gao_search = re.compile(r'^[a-zA-Z]{1}\d{5}[.]?\d*$')
gan_search = re.compile(r'^[a-zA-Z]{2}\d{6}[.]?\d*$')
#gene identifier seems to be 4 characters starting with letters
gid_search = re.compile(r'^\w{4,5}')
#protein product name follows much looser characteristics "else"
#ppn_search = re.compile(r'^')

for line in test:
	#print(line)
	thing = loc_search.search(line)
	if thing != None:
		print(thing, "chromosomal location")
	else:
		pass
	thing = gao_search.search(line)
	if thing != None:
		print(thing, "gene accession (old)")
	else:
		pass
	thing = gan_search.search(line)
	if thing != None:
		print(thing, "gene accession (new)")
	else:
		pass
	thing = gid_search.search(line)
	if thing != None:
		print(thing, "gene id")
	else:
		print(thing, "protein product probably")
	#thing = ppn_search.search(line)
	#if thing != None:
	#	print(thing, "protein product name")
	#else:
	#	print("No match")