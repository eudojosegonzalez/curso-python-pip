import csv
import os 
import matplotlib.pyplot as plt
import random

os.system('clear')

def generat_bar_chart():
  labels=['a','b','c']
  x=random.randrange(1,1000)
  y=random.randrange(1,1000)
  z=random.randrange(1,1000)
  values=[x,y,z]
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  n=str(random.randrange(1,500))
  plt.savefig(f'archivo{n}.png')
  plt.close()

if __name__ == '__main__':
  generat_bar_chart()