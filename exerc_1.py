#!/usr/bin/python
#coding=utf-8

''' 
criar um programa para converter um valor em segundos para um valor em horas, minutos e segundos
'''

valor = input ('Insira o valor em segundos ')
valor = int(valor)


if valor >= 60 :
	minutos = int (valor / 60)
	segundos = valor % 60
	

	if minutos >= 60 :
		horas = int (minutos / 60)
		minutos = minutos % 60
		print (f'{valor} segundos é igual a {horas}:{minutos}:{segundos}')
	else:
		print (f'{valor} segundos é igual a 0:{minutos}:{segundos}')

else :
	minutos = 0
	print (f'{valor} é igual a 0:0:{valor}')



