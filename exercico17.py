#verificação de maior de idade
ano_atual=int(input("insira o ano atual: "))
ano_nasc=int(input("Insira o ano do seu nascimento: "))
aniver=int(input("Você já fez aniversário este ano? 1-Sim 2-Não: "))
if aniver == 1:
    idade=ano_atual-ano_nasc
else:
    idade=ano_atual-ano_nasc-1
if idade>=18:
    print("Você é maior de idade")
else:
    print("Você não é maior se idade")
print(f"Você tem {idade} anos")