import csv

#longest common subsequence algo
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result



reader = csv.reader(open('Population data with GP codes.csv'))
d = {}
for row in reader:
	row[10] = row[10].strip()
	d[ ( row[10].strip()).lower() ] = (row[12], row[13])


reader = csv.reader(open('GPs_unmatched.csv'))
gp_names_unmatched = []
for row in reader:
	gp_names_unmatched.append(row[0].lower())

#keys_in_d = []
#keys_in_d = d.keys()

#for key in d.keys(): 
#	print key 


matched_string_list = []

for row in gp_names_unmatched:
#	print row 
	max_match = 0
	matched_string = None
	for key in d.keys():
		#print (row,key)
		set_value = lcs (row.lower(),key)  
		#print str
		if len(set_value) > max_match:
			#print ( len(set_value), key)
			max_match = len(set_value)
			matched_string = key
	if d.get(matched_string) != None:
	
		print row, ', '.join(d.get(matched_string))		
	#print(matched_string,row)	
	#matched_string_list.append(matched_string)	


'''for line in matched_string_list:
	print line
		
		str = lcs(row.lower(),key)
		if len(str) > max_match:
			print len (str)
			print("\n")
			max_match = len(str)
			matched_string = str
			print matched_string





'''
