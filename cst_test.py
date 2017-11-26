import csv
open_file = False
while(not open_file):
	file_name = raw_input("what file?:")
	try:
		print file_name
		fobj = open(file_name,"rU")
		open_file = True
	except IOError:
		print "Error,try again"

f_csv = csv.reader(fobj)
sheet = []
for row in f_csv:
	sheet.append(row)
print sheet
fobj.close()
sheet[2][2] = "52"
sum_flt = 0
for g in sheet[2][1:-1]:
	sum_flt += float(g)
avg = sum_flt/3
sheet[2][4] = '%.2f'%avg 

fobj = open("csv_test.csv","w")
f_csv_w = csv.writer(fobj)
for row in sheet:
	f_csv_w.writerow(row)
fobj.close()