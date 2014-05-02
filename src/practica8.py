#!/usr/bin/python
#!encoding: UTF-8
import moduloerror
import sys
if((len(sys.argv)==1) or (len(sys.argv)==2)or(len(sys.argv)==3)):
  print ("No se han introducido los valores necesarios. Se utilizarán los valores predeterminados:")
  print("Intervalos= 10  Veces=10  umbral 0.1")
  k=10
  n=10
  umbral=0.1
else:
  n= int(sys.argv[2])
  k= int(sys.argv[1])
  umbral=float(sys.argv[3])
print("Nº de intervalos\tNº de veces\tUmbral de error\tPorcentaje")
print "       %d,                  %d,               %g,          %g" %(k, n, umbral, moduloerror.error (n, k, umbral))    