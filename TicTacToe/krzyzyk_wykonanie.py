#usr/bin/python3
# -*- coding: utf-8 -*-
import krzyzyk
import sys

def gra():
   while True:
      #Menu i Wybieranie strony
      krzyzyk.menu()
      strony_tab = krzyzyk.wybierz()
      strona1 = strony_tab[0]
      strona2 = strony_tab[1]

      #Ruch Strony1
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona1)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      wygrana = krzyzyk.sprawdz(strona1)
      if(wygrana):
         break
      
      
      #Ruch Strony2
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona2)
      krzyzyk.wstaw(numer,strona2)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona2)
      wygrana = krzyzyk.sprawdz(strona2)
      if(wygrana):
         break
      
      #Ruch Strony1
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona1)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona1)
      wygrana = krzyzyk.sprawdz(strona1)
      if(wygrana):
         break
      
      #Ruch Strony2
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona2)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona2)
      wygrana = krzyzyk.sprawdz(strona2)     
      if(wygrana):
         break
      
      #Ruch Strony1
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona1)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona1)
      wygrana = krzyzyk.sprawdz(strona1)
      if(wygrana):
         break
      
      #Ruch Strony2
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona2)
      krzyzyk.wstaw(numer,strona2)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona2)
      wygrana = krzyzyk.sprawdz(strona2)
      if(wygrana):
         break
      
      #Ruch Strony1
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona1)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona1)
      wygrana = krzyzyk.sprawdz(strona1)
      if(wygrana):
         break
      
      #Ruch Strony2
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona2)
      krzyzyk.wstaw(numer,strona2)
      krzyzyk.plansza_wyswietl()
      
      if(krzyzyk.sprawdz(strona2)):
         sys.exit(0)
         break
      
      #Ruch Strony1
      
      krzyzyk.plansza_wyswietl()
      numer = krzyzyk.wpisz_numer(strona1)
      krzyzyk.wstaw(numer,strona1)
      krzyzyk.plansza_wyswietl()
      krzyzyk.sprawdz(strona1)
      wygrana = krzyzyk.sprawdz(strona1)
      if(wygrana):
         break
      
      print("Nikt nie wygrał!")
      
   return None


gra()
