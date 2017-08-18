import csv	
import operator 
import copy
from token import EQUAL
from __builtin__ import sorted

reader = csv.reader(open('C:\Users\kulka\Desktop\Largest_Cities_CSV(1).csv'), delimiter="," )


u = 'State - Place'
x = 'Year'
y = 'Population'
z = 'Kulkarni - Rank'
rows_so_far  = 0
c = 0

pool =  []

pool.append([])

for row in reader:
	if rows_so_far ==0:
		rows_so_far += 1
		header = row
		for j in range (0, 4):
			if j==0:
				pool.append([])
				pool[0].append(u)
			if j==1:
				pool[0].append(x)
			if j==2:
				pool[0].append(y)
			if j==3:
				pool[0].append(z)
	else:
		for i in range(len(row)-2):
			a = len(pool)
			if not row == []:
				if i==0 or i>=1:
					item = copy.deepcopy(row)
					r	 = copy.deepcopy(row)
				
				
				for j in range(0, 4):
					if item[i+2] is not '':
						if j==0:
							r[0] = item[j+1]+' - '+item[j]
							pool.append([])
							pool[a-1].append(r[0])
						if j==1:
							pool[a-1].append(int(header[i+2]))
												
						if j==2:
							if item[i+2] == '':
								pool[a-1].append(int(0))
							else :
									pool[a-1].append(int(item[i+2]))
									
						if j==3:
							pool[a-1].append(int(0))
	rows_so_far += 1
	
a = len(pool)

list = pool[1:a-1]

list.sort(key=lambda b: (b[1],b[2]), reverse=True)

list1 = []
list1.append([])
list1[0] = pool[0]
list1[1:a-1] = list[0:a-2]

mycsv = csv.writer(open('C:\Users\kulka\Desktop\Siddharth Kulkarni.csv', 'wb'))
for row in list1:

	e = list1.index( row )
	
	if row[1] <> c and e <> 0:
		v = 1
		c = row[1]
		row[3] = v
	else:
		if row[1] == c and e <> 0:
			v+=1
			row[3] = v
		
	mycsv.writerow(row)