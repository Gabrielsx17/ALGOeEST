palavras = []

# Lista para armazenar os palíndromos encontrados
palindromos = []

# Coletar 5 palavras do usuário
for i in range(5):
    palavra = input(f"Digite a {i + 1}ª palavra: ").lower()  # Convertendo para minúsculas
    palavras.append(palavra)

# Verificar quais palavras são palíndromos
for palavra in palavras:
    if palavra == palavra[::-1]:  # Verifica se é igual ao inverso
        palindromos.append(palavra)

# Exibir as palavras que são palíndromos
print("\nPalavras palíndromas encontradas:")
if palindromos:
    for p in palindromos:
        print(p)
else:
    print("Nenhuma palavra palíndroma foi encontrada.")