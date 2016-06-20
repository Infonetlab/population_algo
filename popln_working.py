import csv

#Read population data
reader = csv.reader(open('Population data with GP codes.csv'))
d = {}
for row in reader:
	row[10] = row[10].strip()
	d[ ( row[10].strip()).lower() ] = (row[12], row[13])
	    
#Read GP data
reader = csv.reader(open('thane_GP_data_orig.csv'))
gp_names = []
for row in reader:
	row[6] = row[6].strip()
	gp_names.append(row[6].lower()) 


#primary match of Gp data with population data and print population for matched GPs
count = 0
for gp_name in gp_names:
	if d.get(gp_name) != None:
		print gp_name, ', '.join(d.get(gp_name))
		#file.write("%s %s \n"  ( gp_name, ', '.join(d.get(gp_name)) ) ) 
		count+=1

#print unmatched GPs to a file
file = open("GPs_unmatched_op.txt", "w")
for gp_name in gp_names:
	if d.get(gp_name) == None: 
		file.write(gp_name)
		file.write("\n")
file.close()

print "matched GPs", count
print "population data",len(d)

