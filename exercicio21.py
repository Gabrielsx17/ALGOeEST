soma=0
e=0
numeros=[]
for i in range (0,10):
    e=i+1
    numeros.append(int(input(f"Insira o {e}° número da lista: ")))
# print(numeros)
i=0
for i in range (0,10):
    soma=soma+numeros[i]
print(soma)
