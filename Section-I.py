#!usr/bin/env python
import re
f1= open("mutect_immediate.vcf",'r')
f2= open("truseq.bed",'r')
f3= open("accepted.txt",'w') #Written the results to text format which can be opened in excel
l=[]
panel = dict()
for j in f2: #opening file truseq.bed and creating dictionary for the panel regions of each chromosome position
	temp2 = j.split()
	if temp2[0] in panel:
	   	panel[temp2[0]].append([int(temp2[1]),int(temp2[2])])
    	else:
        	panel[temp2[0]] = [[int(temp2[1]),int(temp2[2])]]
for i in f1: #opening file mutect_immediate.vcf and searching the chromosome positions with the panel regions stored in the dictionary
	if not re.search('^#.*',i):
		temp = i.split()
		if temp[0] in panel:
			l=panel.get(temp[0])
			for k in l:
				if int(k[0]) <= int(temp[1]) <= int(k[1]):
					f3.write(str(i)) #writing accepted mutations to new file
f1.close()
f2.close()
f3.close()


