f = open("intraree.txt", "r")
Line = f.readline().split()
n = int(Line[0])
Lista = []
for i in range(n) :
    Line = f.readline().split()
    Lista.append((int(Line[0]), int(Line[1])))
Lista_sorted = sorted(Lista, key = lambda x: -x[1])
print(Lista)
print(Lista_sorted)
suma = 0
count = 0
Ordine = []
Set = set()
for i in range( Lista_sorted[0][1]) :
    while (count < n-1 and Lista_sorted[count][1] == Lista_sorted[count + 1][1]) :
        Set.add(Lista_sorted[count])
        count += 1
    if count < n :
        Set.add(Lista_sorted[count])
        count += 1
    print(Set)
    maxim = max(Set, key = lambda x: x[0])
    suma += maxim[0]
    Set.remove(maxim)
    Ordine.append(Lista.index(maxim)+1)
print(suma)
print(Ordine)