
import sys
import os
import requests
import json
import urllib.request
from time import sleep

sistema = sys.platform

if sistema == "linux" or sistema == "linux2":
	conectar = urllib.request.urlopen("https://www.google.com")
	if conectar:
		while True:
			os.system("clear")
			print('ZIPCODE_SEARCH')
			print(end='\n')
			print('não se esqueça "-" \n')
			cep_user = str(input("\033[1;32m[+]\033[m Informe o CEP para busca: "))
			if "-" not in cep_user:
				print("\n\033[1;32m[ERROR] Você não colocou o - no seu cep. tente novamente!\033[m")
				sleep(3)
				print('Fechando..')
				sleep(2)
				print()
				sys.exit()
			else:
				url = "https://viacep.com.br/ws/{}/json/".format(cep_user)
				requisitar = requests.get(url)
				if requisitar.status_code == 200:
					dados = json.loads(requisitar.text)
					for k,v in dados.items():
						if k == "erro":
							print("\033[1;31m[ERROR]\033[m Esse cep {} é inválido!".format(cep_user))
							sleep(3)
							print('Fechando..')
							sleep(2)
							sys.exit()
					print()
					print("==========================")
					print("  \033[1;32m--> CEP ENCONTRADO <--\033[m")
					print("==========================\n")
					for key,value in dados.items():
						if key and value:
							print("\033[1;32m[INFO]\033[m \033[1;33m{}\033[m: {}".format(key,value))
					print()
					print("S > Sair")
					print("N > Buscar novo CEP\n")
					sair = str(input("\033[1;32m[*]\033[m Deseja pesquisar novo CEP ou deseja sair? [S/N]: ")).upper()
					while sair not in "S" and sair not in "N":
						sair = str(input("\033[1;32m[*]\033[m Deseja pesquisar novo CEP ou deseja sair? [S/N]: ")).upper()
					if sair == "S":
						print("\n\033[1;31m[*]\033[m Saindo...\n")
						sys.exit()
					elif sair == "N":
						pass
	else:
		print("\033[1;31m[ERROR]\033[m Parece que você não está conectado na internet! :(\n")

elif sistema == "win32":
	os.system("cls")
	conectar = urllib.request.urlopen("https://www.google.com")
	if conectar:
		while True:
			os.system("cls")
			print('--'*8)
			print('ZIPCODE_SEARCH')
			print('--'*8)
			print(end='\n')
			print('usar o "-" não se esqueça\n')
			cep_user = str(input("[*] Informe o CEP para busca: "))
			if "-" not in cep_user:
				print("\n[ERROR] Você não colocou o - no seu cep. tente novamente!\n")
				sleep(3)
				print('Fechando..')
				sleep(2)
				sys.exit()
			else:
				url = "https://viacep.com.br/ws/{}/json/".format(cep_user)
				requisitar = requests.get(url)
				if requisitar.status_code == 200:
					dados = json.loads(requisitar.text)
					for k,v in dados.items():
						if k == "erro":
							print("[ERROR] Esse CEP {} é inválido!".format(cep_user))
							sleep(3)
							print('Fechando..')
							sleep(2)
							sys.exit()
					print()
					print("==========================")
					print("  --> CEP ENCONTRADO <--")
					print("==========================")
					print()
					for key,value in dados.items():
						if key and value:
							print("[*] {}: {}".format(key,value))
					print()
					print("S > Sair")
					print("N > Buscar novo CEP\n")
					sair = str(input("[*] Deseja sair ou buscar novo cep? [S/N]: ")).upper()
					while sair not in "S" and sair not in "N":
						sair = str(input("[*] Deseja sair ou buscar novo cep? [S/N]: ")).upper()
					if sair == "S":
						print("\n[*] Saindo...\n")
						sys.exit()
					elif sair == "N":
						pass
	else:
		print("[ERROR] Parece que você não está conectado na internet! :(\n")
else:
	print("\033[1;31m[ERROR] Esse script não te versão para esse sistema! :(\n\033[m")
