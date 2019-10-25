f = open("intrare.txt", "r")
Line = f.readline().split()
n = int(Line[0])
p = int(Line[1])
Cuburi = []
for i in range(n) :
    Line = f.readline().split()
    Cuburi.append([int(Line[0]), int(Line[1])])
Cuburi_Sorted = sorted(Cuburi,key = lambda x: x[0], reverse = True )
print(Cuburi)
print(Cuburi_Sorted)
Ordine = []
s = Cuburi_Sorted[0][0]
index = 1
Ordine.append(Cuburi.index(Cuburi_Sorted[0])+1)
i =1
for i in range(n) :
    if(Cuburi_Sorted[i][1] != Cuburi_Sorted[i-1][1]) :
        s += Cuburi_Sorted[i][0]
        index += 1
        Ordine.append(Cuburi.index(Cuburi_Sorted[i])+1)
print(index, s)
print(Ordine)
f.close()
