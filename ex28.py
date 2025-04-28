imp=[]
par=[]
lista=[]
for i in range(0,8):
    lista.append(int(input("insira um numero inteiro")))
for e in range(0,7):
    if lista[e]%2==0:
        par.append(lista[e])
    else:
        imp.append(lista[e])
print(par)
print(imp)