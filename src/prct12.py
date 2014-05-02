#ecoding: UTF-8
#!/usr/bin/python

import platform
import os
import moduloaproximacion
import moduloerror
import time
import timeit

def informacionsoftware():
  softinfo={}
  softinfo={'several':platform.uname() , 'S.O':platform.platform, 'Pythons Version' :platform.python_version(), 'Date' :platform.python_build()}
  return softinfo
  
def InformacionCPU():
  infofile = '/proc/cpuinfo'
  cpuinfo = {} 
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpuinfo['CPU type'] = value
      elif name == 'cache size':
	cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
	cpuinfo['CPU speed'] = value + ' Hz '
      elif name == 'vendor_id':
	cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo
    
if __name__ == '__main__':
  softinfo = informacionsoftware()
  for keys in softinfo.keys():
    print softinfo[keys]
  cpuinfo = InformacionCPU()
  for keys in cpuinfo.keys(): 
    print cpuinfo[keys]

  print"Introduzca el nombre del fichero para guardar los resultados:"
  nombre_fichero = raw_input ();
  f = open(nombre_fichero,"w")
  f.write('Hola')
  for keys in softinfo.keys():
    if type (softinfo[keys])is list:
      f.write('\n'.join(softinfo[keys]))
    else: 
      f.write(str(softinfo[keys]))
      f.write('\n')
  for keys in cpuinfo.keys():
    if type (cpuinfo[keys]) is list:
      f.write('\n'.join(cpuinfo[keys]))
    else:
      f.write(str(cpuinfo[keys]))
      f.write('\n')
  f.close()
  
	
  print "Introduzca cinco umbrales de error:"
  umbral =[]
  n=10
  k=10
  for i in range(5):
    print "Introduzca el umbral", i, ":"
    umbral.append(float(raw_input()));
  print"Introduzca el nombre fichero donde desea almacenar los resultados"
if (n>0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write("num de intervalos: %d\n"%(n))
  for i in range (5):
    start=time.time()
    moduloerror.error(n, k, umbral[i])
    finish=time.time() - start
    t1=timeit.Timer('modulo.error(n.k,umbral)',setup='import modulo.error')
    t1.timeit(10000000)
    print t1.timeit(10)
    fichero.write("%2.10f\n"%(finish))
    fichero.close()
  else:
    print "No puede haber intervalos menores que 0"