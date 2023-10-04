import mod
import random
import os 

  
paises =[
  {
    'Country':'Colombia',
    'Population':1000
  },
  {
    'Country':'Venezuela',
    'Population':2000
  },
  {
    'Country':'Peru',
    'Population':3000
  }  
]

# esto permite aislar lo ejecutable de las definciones
def run():
  os.system('clear')
  
  print(mod.get_population())
  
  keys, values = mod.get_population()
  print (keys)
  print (values)
  
  country=input ('Que pais?=>')
  result=mod.population_by_country(paises,country)
  print (result)

if __name__ == '__main__':
  run()