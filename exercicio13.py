#Cadastro alunos da escola, deve conter, nome, idade e turma
print("Cadsatre-se:")
nome=input("Insira seu nome: ")
idade=int(input("Sua idade: "))
turma=input("Qual turma você pertence: ")
if idade>6:
    print(f"Aluno cadastrado com sucesso: {nome}, {idade} anos, turma {turma}. ")
else:
    print("Você é novo demais para se matricular")