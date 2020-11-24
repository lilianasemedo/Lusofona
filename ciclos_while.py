#!/usr/bin/python
#coding=utf-8

#ciclo while


lista = ["windows", "macos","linux","solaris","android","ios"]
tamanho = len(lista)-1


arquivo2 = open('arquivo2.txt', 'w')

while tamanho > -1:

	if tamanho == -1:
		break

	if lista[tamanho] == "solaris":
		pass

	
	else:
		print(lista[tamanho])
		arquivo2.write(lista[tamanho])
		arquivo2.write("\n")
	
	tamanho -= 1

arquivo2.close()

