soma=0
media=0
numeros=[]
for i in range (0,5):
    e=i+1
    numeros.append(float(input(f"Insira a {e}° nota: ")))
    soma=soma+numeros[i]
media=soma/5
print(media)