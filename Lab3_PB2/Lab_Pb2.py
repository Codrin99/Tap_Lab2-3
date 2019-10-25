f = open("date.txt", "r")
fr_cuv = []
lungimi = []
list = []
dict = {}
lungimi = f.readline().split()
fr_cuv = f.readline().split()
for i in range(0,len(lungimi)):
    pereche = (int(lungimi[i]), int(fr_cuv[i]))
    list.append(pereche)
pozitie = 1
for pereche in list:
    dict[pereche] = pozitie
    pozitie += 1
list.sort(key = lambda x: (x[1], -x[0]), reverse = True)
print(list)
timp = 0
suma = 0
for pereche in list:
    suma += pereche[0]
    timp = timp + pereche[1] * suma
print(timp)
for pereche in list:
    print(dict[pereche], end = ' ')
f.close()