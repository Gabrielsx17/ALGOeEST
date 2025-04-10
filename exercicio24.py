numeros=[]
numeros.append(int(input(f"Insira o 1° número: ")))
maior=numeros[0]
menor=numeros[0]
for i in range (1,5):
    e=i+1
    numeros.append(int(input(f"Insira o {e}° número: ")))
i=0
for i in range (0,5):
    if numeros[i]>maior:
        maior=numeros[i]
    elif numeros[i]<menor:
        menor=numeros[i]
print(f"O maior numéro foi {maior} e o menor foi {menor}")

