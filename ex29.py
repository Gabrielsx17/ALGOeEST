valores = []

# Coletar os 4 números inteiros do usuário
for i in range(4):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    valores.append(num)

# Solicitar o número adicional para multiplicação
multiplicador = int(input("Digite um número para multiplicar os valores da lista: "))

# Multiplicar cada elemento da lista pelo número fornecido
for i in range(len(valores)):
    valores[i] *= multiplicador  # Atualiza o valor diretamente na lista

# Exibir os novos valores da lista
print("\nValores multiplicados:")
for valor in valores:
    print(valor)