import csv

from new_girl import girl
from new_boy import boy
from utility import testing_utility
from log import generator_log

testing_utility()
boy_s = open('LADKA.csv')
get_boys = csv.reader(boy_s, delimiter = ',')
girl_s = open('LADKI.csv')
get_girls = csv.reader(girl_s, delimiter = ',')
list_girls=[]
list_boys=[]

for z in get_girls:
	list_girls += [girl(z[0],int(z[1]),int(z[2]),int(z[3]),z[4])]


for y in get_boys:
	list_boys += [boy(y[0],int(y[1]),int(y[2]),int(y[3]),int(y[4]),y[5])] 

for x in  list_girls:
	for w in  list_boys:
		generator_log(x.name + '  is searching for ' + w.name)
		if x.status=='single' and w.status=='single' and x.eligibility(w.budget) and w.eligibility(x.maintainance_budget, x.attractiveness) :
			w.girlfriend = x.name
			x.boyfriend = w.name
			x.status = w.status = 'Committed'
						
			print(x.name + '  is committed to ' + w.name)
			generator_log(x.name + '  is committed to ' + w.name)
			break
