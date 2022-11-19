#1
szoveg = input("Kérlek írj egy rövid szöveget!")
print(szoveg.upper())

#2
if (len(szoveg) > 10):
    print(f"A megadott szöveg hossza {len(szoveg)} karakter.")
else:
    print("A megadott szöveg 10 karakternél rövidebb.")

#3
harom = input("Kérlek adj meg egy legalább 3 betűs szót!")
while len(harom) < 3:
    harom = input("Sajnos ez túl rövid, kérlek adj meg egy másik szót!")
print("Köszönöm!")

#4
i = 0
x = ""
while i <= len(szoveg) and x != "a":
    x = str(szoveg[i])
    i += 1
print(f"Az első {x} betű a szöveged {i}. karaktere.")

#5
j = 0
mennyi = 0
while j < len(szoveg):
    x = str(szoveg[j])
    if (x == "a"):
        mennyi += 1
    j += 1
print(f"Összesen {mennyi} darab {x} betű van a szövegedben.")

#6






#vonal alatti 1
nev = input("Kérlek adj meg neveket! Ha szeretnéd ezt befejezni, kérlek nyomj egy @ karaktert.")
lista = []
k = 0
y = 0
while y != "@":
    y = str(nev[k])
    lista.append[nev]
    k += 1
    nev = input("Jöhet a következő név.")
print(lista)


#vonal alatti 2

#vonal alatti 3
