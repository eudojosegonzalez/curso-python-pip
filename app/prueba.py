import csv
import os 
os.system('clear')

vpath = './app/data2.csv'
total=0
with open(vpath,'r') as csvfile:
  reader = list(csv.reader(csvfile,delimiter=","))
 
for key,value in reader:
  t= int(value)
  total += t

print (total)
