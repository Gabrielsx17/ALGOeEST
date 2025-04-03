#média de 
nota1=float(input("Insira a 1° nota: "))
nota2=float(input("Insira a 2° nota: "))
nota3=float(input("Insira a 3° nota: "))
media=(nota1+nota2+nota3)/3
if media>=7:
    print("Aprovado")
elif media>=5:
    print("Recuperação")
else:
    print("Reprovado")
print(media)
