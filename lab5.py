import os
from os.path import join, getsize
import csv
# for root, dirs, files in os.walk('\\'):
#     print root, "consumes",
#     print sum(getsize(join(root, name)) for name in files),
#     print "bytes in", len(files), "non-directory files"
#     if 'CVS' in dirs:
#         dirs.remove('CVS')  # don't visit CVS directories

index={}

out=open('index.csv','wb')
writer=csv.writer(out)

for root, dirs, files in os.walk("e:"):
    for file in files:
        if file.endswith(".txt"):
        	 f=open(os.path.join(root, file))
        	 for line in f:
        	 	for word in line.split():
        	 		if word in index:
        	 			index[word].append(os.path.join(root, file))
        	 		else:
        	 			index[word]=[os.path.join(root, file)]

        else:
         	fname=os.path.splitext(file)[0]
         	index[fname]=[os.path.join(root, file)]



         	 		#print(os.path.join(root, file))
for key,values in index.items():
	#for value in values:
		#print key+"=>"+value 
	writer.writerow([key,values])


search=input("Enter the word to search:")
if search in index:
	print index[search]
else:
	print "not found"	