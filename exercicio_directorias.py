#!/usr/bin/python
#coding=utf-8

''' 
Criar um programa em python que permita criar, renomear, remover e listar
directorias.

'''

import os
import string
import sys
import errno


def criar():
	
	while 1:	
		
		try:	
			valor = input ('Insira o nome da nova directoria \n')
			os.mkdir(valor)
			print("Nova directoria criada com sucesso")
			break


		except FileExistsError:
			print("Ops !  Directoria já existe. ",end="")

		except FileNotFoundError:
			print("Ops !  Nome inválido. ",end="")
	
		
	

def editar():

	while 1:

		try :

			valor = input ('Digite Antigo nome \n')
			novo_valor = input ('Digite Novo nome \n')
			os.rename(valor,novo_valor)
			print("Directoria renomeada com sucesso \n")
			break	

		except FileNotFoundError:
			print("Ops !  Directoria nao encontrada. ",end="")
		
		except Exception as erro:
			print("Ops ! Não é possivel, a directoria não está vazia ", end="")

		


					

def listar():
	
	path = os.getcwd()
	direc = os.listdir(path)
	print(f'{direc} \n')

	
	
def remover():
	while 1:	
		
		try:	
			valor = input ('Insira o nome da directoria \n')
			os.rmdir(valor)
			print("Directoria removida com sucesso. \n")
			break


		except FileNotFoundError:
			print("Ops ! Directoria nao encontrada. ",end="")


		except Exception as erro:
			print("Ops ! Não é possivel, a directoria não está vazia ", end="")

				
	
		
	




while 1:


	valor = input ('Escolha um dos seguintes comandos: criar, editar, listar e remover  \n')


	if valor == 'criar':
		res = criar()
		break

	elif valor == 'editar':
		res = editar()
		break

	elif valor == 'listar':
		res = listar()
		break

	elif valor == 'remover':
		res = remover()
		break

	else:
		print("a opçao não é correcta")
		



