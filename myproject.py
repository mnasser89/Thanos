import os 
import random
#from  functools import *
os.chdir('D:\\myporject\\Thanos\\Universe')
myuniverse= os.listdir()
num_unvierse=len(myuniverse)
delteted_universe=[]
x = input ('Do u want to destroy half of unvierse: y or n > ').lower()
if x== 'y':   
 for i in range (1,26):
   if num_unvierse > 25 :
    
        myuniverse= os.listdir()
        num_unvierse=len(myuniverse)
        select_unvires = random.choices(os.listdir())
        destroy= (select_unvires[0])
        os.remove(destroy)
        delteted_universe.append(select_unvires)   

    
 print ('we already detroy half of universe ')
if len(delteted_universe)>0:
        for i in delteted_universe:
            print ('we destroy {}'.format(i))
if num_unvierse ==25:
    print ("it's already destroyed")
 
