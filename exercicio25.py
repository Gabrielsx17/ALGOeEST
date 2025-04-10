palpites=[]
palpite=0
i=0
import random
random_integer=random.randint(1,20)
palpite=int(input("Faça o seu palpite: "))
palpites.append(palpite)
if random_integer!=palpite:
    i=1
    while palpite!=random_integer:
        print("Você errou!!")
        palpite=int(input("Faça o seu palpite: "))
        palpites.append(palpite)
        i=i+1
else:
    print(f"Você acertou!!, o número certo era{random_integer}")
    print(f"Estes foram seus palpites {palpite}")
print(f"Você acertou!!, o número certo era {random_integer}")
print(f"Estes foram seus palpites {palpites}")

