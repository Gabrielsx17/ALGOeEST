palavras=[]
nummaiorque5=0
i=0
while i < 6:
    palavras.append (input("Insira a palavra:"))
    i+=1
i=0
for i in range (0,5):
    if len(palavras[i])>5:
        nummaiorque5=1+nummaiorque5
    i+=1
print(f"{nummaiorque5} palavras sao maiores que 5 letras")
