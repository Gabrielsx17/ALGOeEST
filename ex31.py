def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")
tabuada(int(input("Insira o numero a ser calculado: ")))