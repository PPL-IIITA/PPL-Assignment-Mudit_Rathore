import random
import csv
import pprint
import logging
import math

from utility import testing_utility 
from miser import miser 
from geek import geek 
from generous import generous 
from choosy import choosy 
from essential import essential 
from luxury import luxury 
from desperate import desperate 
from normal import normal  
from couples import couples 
from log import generator_log 
from new_boy import boy 
from new_girl import girl 
from gift import gift 
from util import util 

logging.basicConfig(filename='log_text.log',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s; %(message)s',level = logging.DEBUG,filemode='w')

def calculate_happiness(pair):
	fp1 = open('gifts_list.csv','r')
	read = csv.reader(fp1,delimiter=',')
	gifts = []
	for i in fp1:
		if(i[3] == 'luxury'):
			gifts += [luxury(i[0],int(i[1]),int(i[2]),i[3])]
		elif (i[3]=='util'):
			gifts += [util(i[0],int(i[1]),int(i[2]),i[3])]
		elif (i[3]=='essentials'):
			gifts += [essential(i[0],int(i[1]),int(i[2]),i[3])]
	gifts = sorted(gifts,key = lambda item: item.cost)
	logging.warning('\nDetails:\n')
	for i in pair:
		if(i.boy._type == 'miser'):
			miser(gifts,i)

		if(i.boy._type == 'generous'):
			generous(gifts,i)

		if(i.boy._type == 'geek'):
			geek(gifts,i)
	detail_gift(pair)

def happy_couple(pair,index):
	A = sorted(pair, key=lambda item: item.happiness, reverse = True)
	B = sorted(pair, key=lambda item: item.compatibility, reverse = True)
	print('\n\n' + str(index) + 'most Comapitible are:')
	for j in range(index):
		print(B[i].boy.name + '&' + A[i].girl.name)
	print('Beware\n')
	print('\n\n' + str(index) + 'happy couples:\n')
	for j in range(index):
		print(A[i].boy.name + '&' + B[i].girl.name)
	print('Beware\n\n\n\n')

def generous(gift,qw):
	A = 0
	B = 0
	for j in gifts:	
		if(qw.boy.budget - j.cost > 0) and (qw.boy.budget >= 0) and ((qw.boy.budget - j.cost <=300) or (j.cost == qw.boy.budget)):
			if(j._type == 'luxury'):
				B = B + 2*j.cost
			else:
				B = B + j.cost
			A = A + j.cost
			qw.gifts = qw.gifts + [j]	
			qw.boy.budget = qw.boy.budget - j.cost 
			logging.info(qw.boy.name + ' gave ' + qw.girl.name + 'a gift ' + j.name + 'of price = Rs. ' +str(j.cost) + '\-.')
	if(qw.girl._type == 'choosy' and B>0):
		qw.girl.happiness = math.log10(B)
	elif(qw.girl._type == 'normal'):
		qw.girl.happiness = A
	else:
		qw.girl.happiness = math.exp(A)
	qw.boy.happiness = qw.girl.happiness
	qw.set_happiness()
	qw.set_compatibility() 			

def miser(gift,qw):
	A = 0
	B = 0
	for j in gifts:	
		if(qw.boy.budget >= 0) and ((j.cost - qw.boy.budget <= 100)or j.cost == qw.girl.budget) and (qw.boy.budget - j.cost > 0):
			if(j._type == 'luxury'):
				B = B + 2*j.cost
			else:
				B = B + j.cost
			A = A + j.cost
			qw.gifts = qw.gifts + [j]	
			qw.boy.budget = qw.boy.budget - j.cost 
			logging.info(qw.boy.name + ' gave ' + qw.girl.name + 'a gift ' + j.name + 'of price = Rs. ' +str(j.cost) + '\-.')
	if(qw.girl._type == 'choosy' and B>0):
		qw.girl.happiness = math.log10(B)
	elif(qw.girl._type == 'normal'):
		qw.girl.happiness = A
	else:
		qw.girl.happiness = math.exp(A)
	qw.boy.happiness = qw.girl.happiness
	qw.set_happiness()
	qw.set_compatibility()

def geek(gift,qw):
	A = 0
	B = 0
	for j in gifts:	
		if(qw.boy.budget >= 0) and ((j.cost - qw.boy.budget <= 100) or j.cost == qw.girl.budget) and (qw.boy.budget - j.cost > 0):
			if(j._type == 'luxury'):
				B = B + 2*j.cost
			else:
				B = B + j.cost
			A = A + j.cost
			qw.gifts = qw.gifts + [j]	
			qw.boy.budget = qw.boy.budget - j.cost 
			logging.info(qw.boy.name + ' gave ' + qw.girl.name + 'a gift ' + j.name + 'of price = Rs. ' +str(j.cost) + '\-.')
	for u in gifts:
		if( i not in qw.gifts) and (i._type == 'luxury') and (i.cost <= qw.boy.budget):
			B = B +2*i.cost
			A = A + i.cost
			qw.gifts = qw.gifts + [i]
			qw.boy.budget = qw.boy.budget - i.cost
			generator_log(qw.boy.name + 'gave ' + qw.girl.name + 'a gift: ' + i.name + 'of price = Rs.' + str(i.cost) + '/-,')
			break
 
	if(qw.girl._type == 'choosy' and B>0):
		qw.girl.happiness = math.log10(B)
	elif(qw.girl._type == 'normal'):
		qw.girl.happiness = A
	else:
		qw.girl.happiness = math.exp(A)
	qw.boy.happiness = qw.girl.happiness
	qw.set_happiness()
	qw.set_compatibility()

def detail_gift(pair):
	for j in pair:
		print('Gifts presented to' + j.girl.name + 'from'  + j.boy.name)
		for  i in j.gifts:
			print(i.name + '   type: ' + i._type)
		print('\n')
		index = random.randint(1,len(pair))
	happy_couple(pair, index)


def test():
	fp1 = open('LADKA.csv','r')
	read = csv.reader(fp1,delimiter=',')
	boys_list = []
	for j in fp1:
		if(j[5] == 'miser'):
			boys_list += [miser(j[0],int(j[1]),int(j[2]),int(j[3]),int(j[4]),j[5])]
		elif(j[5] == 'geek'):
			boys_list += [geek( j[0]),int(j[1]),int(j[2]),int(j[3]),int(j[4]),j[5] )]
		elif(j[5] == 'generous'):
			boys_list += [generous(j[0]),int(j[1]),int(j[2]),int(j[3]),int(j[4]),j[5])]	
	
	fp2= open('LADKI.csv','r')
	readr = csv.reader(fp2,delimiter=',')
	girls_list = []
	for j in fp2 :
		if(j[4] == 'normal'):		
			girls_list += [normal(j[0]),int(j[1]),int(j[2]),int(j[3]),j[4])]
		elif(j[4] == 'desperate'):		
			girls_list += [desperate(j[0]),int(j[1]),int(j[2]),int(j[3]),j[4])]
		elif(j[4] == 'choosy'):		
			girls_list += [choosy(j[0]),int(j[1]),int(j[2]),int(j[3]),j[4])]	

	couples_list = []

	logging.warning('\n\nGirls are searching boys for relationship.\n')
	
	for j in girls_list:
		for k in boys_list:
			generator_log(j.name +' is searching for ' + k.name)
			if k.status == 'single' and j.status == 'single' and (j.eligibility(k.budget) and k.eligibility(j.maintainance_budget,j.attractiveness)):
				j.status = 'committed'
				k.status = 'committed'
				j.boyfriend = k.name
				k.girlfriend = j.name
				generator_log(j.name+'is committed to ' + k.name)		
				logging.warning('Beware')
				couples_list = couples_list + [(j,k)]
				break
	logging.warning('Beware')
	print('\n Commited Couples are :\n')
	for j in girls_list: 
		if j.status == 'committed':
			print(j.name + 'is committed to ' + j.boyfriend)
		else:
			print(j.name + 'is single.\n')
	pair = []
	for j in couples_list:
		pair += [couples()]
	calculate_happiness(pair)
	newly_committed = []
	alt = random.randint(1,len(pair)-1)
	for j in range(alt):
		newly_committed.append(pair[i])
	for j in pair[0:alt]:
		print(j.boy.name + 'broke with' + j.girl.name)
		j.boy.status = 'single'
		j.girl.status = 'single'
		j.pop(0)
	for w in newly_commited:
		j = w.girl
		for q in boys_list:
			generator_log(j.name + 'is looking for ' + q.name)
			if q.name != w.boy.name and q.status =='single' and j.status == 'single' and (j.eligibility(q.budget)) and (q.eligibility(j.budget,j.attractiveness)):
				j.status = 'committed'
				q.status = 'committed'
				j.boyfriend = q.name
				q.status = j.name
				generator_log(j.name + 'Committed to '+ q.name)
				logging.warning('Beware')
				couples_list += [(q,j)]
				break
	for j in girls_list:
		for i in boys_list:
			generator_log(j.name + 'is looking for ' + i.name)
			if i.status == 'single' and j.status == 'single' and (j.eligibility(budget)) and (i.eligibitlity(j.budget,j.attractiveness)):
				j.status = 'committed'
				i.status = 'committed'
				j.boyfriend = i.name
				i.girlfriend = j.name
				generator_log(j.name + "committed to " + i.name)
				logging.warning('Beware')
				couples_list += [(q,j)]
				break
	logging.warning('Beware')
	for j in girls_list:
		if j.status == 'committed':
			print(j.name + 'is committed to ' + j.boyfriend)
		else":
			print(j.name + 'is single ')

	print('Beware')
			
testing_utility()
test()			
