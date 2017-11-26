def weight_grade(grade_list,weight_tulpe = (0.3,0.3,0.3)):
	'''Return the sum'''
	result_float = \
		(grade_list[0]*weight_tulpe[0])+\
		(grade_list[1]*weight_tulpe[1])+\
		(grade_list[2]*weight_tulpe[2])
	return result_float
#########################################################################
def grade(fileline_str):
	field_list = fileline_str.split(",")
	name_str = field_list[1]+" "+field_list[0]
	grade_list = []
	for element_int in field_list[2:]:
		grade_list.append(int(element_int))
	#total_grade_float = weight_grade(grade_list)
	return (name_str,total_grade_float)

############################################################################
def main():
	filename_str = raw_input("Open what file")
	file_obj = open(filename_str,'r')
	print("%-15s%-15s"%("Name","Grade"))
	print("-"*25)
	for file_line in file_obj:
		file_line = file_line.strip()
	#	print file_line
		#print("%-15s%7.2f"%grade(file_line))