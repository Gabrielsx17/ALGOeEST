def tabuada_personalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} a {fim}:")
    for j in range (inicio, fim+1):
        print(f"{base} x {j} = {base*j}")

base=(int(input("Insira a base: ")))
inicio=(int(input("Insira o inicio: ")))
fim=(int(input("Insira o fim: ")))
tabuada_personalizada(base, inicio, fim)