import random
import csv

def testing_utility():
    gift_type = ['Essential','Luxury','Utility']
    girls_type = ['Choosy','Normal','Desperate']
    boys_type = ['Miser','Generous','Geeks']

    gifts = []
    girls = []
    boys = []

    for i in range(0,600):
        gifts = gifts + [('gift' + str(i),random.randint(0,600),random.randint(0,600),gift_type[random.randint(0,2)])]
        #[gift number , , , gift type] 
    for j in range (0,500):
        girls+=[('girl' + str(j),random.randint(0,25),random.randint(0,20),random.randint(0,10),girls_type[random.randint(0,2)])]
        #[name,attractiveness,maintainance_budget,intelligence,_type]
    for k in range(0,1000):
        boys = boys + [('boy' + str(k),random.randint(0,25),random.randint(0,20),random.randint(0,10),random.randint(0,25),boys_type[random.randint(0,2)])]
        #[name,attractiveness,girlfriend_budget,intelligence,minimum_attraction_requirement,boy type ]
    fp1=open('LADKA.csv','w')
    write=csv.writer(fp1,delimiter=',')
    for w in boys:
        write.writerow(w)
    fp2=open('LADKI.csv','w')
    writer=csv.writer(fp2,delimiter=',')
    for v in girls:
        writer.writerow(v)
    fp3=open('GIFT.csv','w')
    writerer=csv.writer(fp3,delimiter=',')
    for z in gifts:
        writerer.writerow(z)
    
   
        
testing_utility()
