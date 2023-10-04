import csv
import os 


def readCsv (path):
  os.system('clear')
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    header=next(reader)
    data=[]
    for  row in reader:
      #unimos las cabeceras con los valores en una lista
      iterable=list(zip(header,row))
      # convertimos la lista de iterables en un diccionario
      country_dic={ key:value for key,value in iterable }

      #apilamos el diccionario en una lista final
      data.append(country_dic)
  # devolvemos la lista resultante
  return (data)



if __name__ == '__main__':
  data= readCsv('./app/data.csv')
  print (data[0])
  print (data[1])
  print (data[2])
  