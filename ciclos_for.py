#!/usr/bin/python
#coding=utf-8

#- o resultado enviar para uma outra lista dentro de um outro ficheiro ficheiro

#ciclo for


arquivo = open('arquivo.txt', 'w')

for var in ["windows", "macos","linux","solaris","android","ios"]:
	if var == "solaris":
		pass
	else:
		arquivo.write(var)
		arquivo.write("\n")

arquivo.close()



