print("VERIFICAÇÃO BANCÁRIA")
saldo=float(input("Insira o saldo da conta: "))
if saldo !=0:
    atividade_da_conta=True
else:
    atividade_da_conta=False
print("Conta ativa") if atividade_da_conta==True else print("Conta inativa") 