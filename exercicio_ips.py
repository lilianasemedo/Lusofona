#!/usr/bin/python
#coding=utf-8

''' 
criar um script em python que cria uma lista com todos os endereços ips 
possiveis na gama 192.168.1.xxx e uma lista com todos os inteiros de 1 a 1024

'''

i_list = []
p_list = []

portList = open('portList.txt', 'w')

for item in range(1024):
	p_list.append(str(item + 1 ))
	portList.write(p_list[item])
	portList.write("\n")
	
	
	
portList.close()	


ipList = open('ipList.txt', 'w')
for item in range(255):
	i_list.append("192.168.1." + str(item + 1))
	ipList.write(i_list[item])
	ipList.write("\n")
	

ipList.close()


