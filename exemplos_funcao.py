# #tabuada do 7
# print("Tabuada do 7")
# for i in range(1,11):
#     print("7 x", i, "=", 7*i)

# #tabuada do 8
# print("Tabuada do 8")
# for i in range(1,11):
#     print("8 x", i, "=", 8*i)

# #tabuada do 9
# print("Tabuada do 9")
# for i in range(1,11):
#     print("9 x", i, "=", 9*i)

#Tabuadas 1 a 10
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")

# #exibindo tabuadas
# # tabuada(1)
# # tabuada(2)
# # tabuada(3)
# # tabuada(4)
# # tabuada(5)
# # tabuada(6)
# # tabuada(7)
# # tabuada(8)
# # tabuada(9)
# # tabuada(10)
# for i in range (1,101):
#     tabuada(i)
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")

def tabuada_personalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} a {fim}:")
    for j in range (inicio, fim+1):
        print(f"{base} x {j} = {base*j}")

base=(int(input("Insira a base: ")))
inicio=(int(input("Insira o inicio: ")))
fim=(int(input("Insira o fim: ")))
tabuada_personalizada(base, inicio, fim)