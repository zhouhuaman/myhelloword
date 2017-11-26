import csv
def read_table(file_handle):
	'''Read Periodic Table file into a dict, with element symbol as key'''
	data_csv = csv.reader(file_handle)
	periodic_dict = {}
	for row in data_csv:
		if row[0].isdigit():
			symbol = row[1]
			periodic_dict[symbol] = row[:8]
	return periodic_dict

############################################################################
def parse_element(element_str):
	'''Parse element string into symbol and quantity, e.g. Si2 returns ("Si",2)'''
	symbol = ""
	quantity_str = ""
	for ch in element_str:
		if ch.isalpha():
			symbol = symbol + ch
		else:
			quantity_str += ch
	if quantity_str = "":
		quantity_str = "1"
	return symbol,int(quantity_str)

################################################################################
#main()
file_handle = open("Periodic-Table.csv","rUb")
periodic_dict = read_table(file_handle)

compoud_str = raw_input("Input a chemical coumpoud, hyphenated,e.g. C-O2: ")
coumpoud_str_list = coumpoud_str_list.split("-")
mass = 0
print "The coumpoud is composed of: "
for c in coumpoud_str_list:
	symbol,quantity_int = parse_element(c)
	print periodic_dict[symbol][5],
	mass += quantity_int * periodic_dict[symbol][6]

print "\n\nThe atomic mass of the compound is ",mass

file_handle.close()
