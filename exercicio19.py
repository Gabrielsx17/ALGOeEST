#anuncio de venda categorias
idade=int(input("Insira a idade: "))
sexo=int(input("Qual seu gênero, 1-Masculino, 2-Feminino: "))
atleta=bool(input("Você é atleta? True-Sim, False-Não: "))

if idade<=15:
    print("Artigos infantís")
elif sexo == 2 and idade<=21:
    print("Maquiagem e moda")
elif sexo == 1 and idade<=32 and atleta == True:
    print("Artigos esportivos")
elif sexo == 1 and idade<=21 and atleta == False:
    print("Videogames")
elif idade>21 and idade<=32 and sexo == 1 and atleta == False:
    print("Oferecer livros, jardinagem e eletrodomesticos")
elif idade>= 22 and idade <=35 and sexo == 2:
    print("Oferecer artigos esportivos e itens de casa")
else:
    print("Não há anuncios adequados a estas caracteristicas")