#usr/bin/python3 
# -*- coding: utf-8 -*-
import sys

plansza = []
for i in range(9):
	plansza.append(i)

def menu():
	print("		")
	print("MENU")
	print("*Wciśnij 1 aby rozpocząć nową grę!*")
	print("*Wciśnij 2 aby wyjść z programu*")
	while True:
		wzor = int(input("Wpisz: "))
		if(wzor == 1):	
			break
		elif(wzor == 2):
			sys.exit(0)
			break
		else:
			print("Zastosuj się do instrukcji!")
			continue
		
	return None

def plansza_wyswietl():
	print("												")
	print("												")
	print("		|		|								")
	print("	%s	|	%s	|	%s	" % (plansza[0], plansza[1], plansza[2]))
	print("		|		|								")
	print("----------------|---------------|----------------")
	print("		|		|								")
	print("	%s	|	%s	|	%s 	" % (plansza[3], plansza[4], plansza[5]))
	print("		|		|								")
	print("----------------|---------------|----------------")
	print("		|		|								")
	print("	%s	|	%s	|	%s	" % (plansza[6], plansza[7], plansza[8]))
	print("		|		|								")
	return None

def wpisz_numer(strona):
	while True:
		try:
			print("														")
			numer = int(input("\nWybierz numer aby wstawić tam "+strona+": "))
			print("														")
		except:
			print("Zastosuj się do instrukcji!")
			continue
		break
	return numer

def wyswietl(plansza):
	j = 0
	for i in plansza:
		print("Miejsce numer %s: %s" %(j, i)) 
		j = j+1
	return None

def wstaw(numer, strona):
	plansza[numer] = strona
	return plansza

def sprawdz(strona):
	if(plansza[0] == strona and plansza[1] == strona and plansza[2] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
		
	if(plansza[3] == strona and plansza[4] == strona and plansza[5] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
		
	if(plansza[6] == strona and plansza[7] == strona and plansza[8] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
	
	if(plansza[0] == strona and plansza[3] == strona and plansza[6] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True		
	
	if(plansza[1] == strona and plansza[4] == strona and plansza[7] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
	
	if(plansza[2] == strona and plansza[5] == strona and plansza[8] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
	
	if(plansza[2] == strona and plansza[4] == strona and plansza[6] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
	
	if(plansza[0] == strona and plansza[4] == strona and plansza[8] == strona):
		print("Grasz %s wygrał!" %(strona))
		return True
	
def wybierz():
	while True:	
		strona = str(input("Wybierz stronę gry, wpisz 'X' albo 'O': "))
		if(strona == 'X' or strona == 'O'):
			if(strona == 'X'):
				strona2 = 'O'
				break
			else:
				strona2 = 'X'
				break

                
		elif(strona == 'x' or strona == 'o'):
			if(strona == 'x'):
				strona2 = 'o'
				break
			else:
				strona2 = 'o'
				break
		
		else:
			print("Zastosuj się do instrukcji!")
			continue
	strony = []
	strony.append(strona)
	strony.append(strona2)
	return strony






