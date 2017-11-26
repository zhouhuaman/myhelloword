import numpy
import pylab as pb
wc_dict = {"dead":4,"great":6}
wc_list = []
for key,value in wc_dict.items():
	if value>2 and len(key)>3:
		wc_list.append((key,value))
wc_list.sort()
key_list = [key for key,value in wc_list]
value_list = [value for key,value in wc_list]

x_axis = numpy.arange(len(wc_list)) 
barwidth = 0.5
pb.xticks(x_axis+barwidth/2.0,key_list,rotation = 45)
pb.bar(x_axis,value_list,width = barwidth, color = "r")
pb.show()