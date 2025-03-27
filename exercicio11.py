print("CADASTRE-SE: ")
email=input("Insira o e-mail desejado: ")
email=str.lower(email)
senha=input("Defina sua senha: ")

if len(senha)>=8:
    print("Senha válida. Cadastro efetuado com sucesso")
    print("Agora que sua conta está cadastrada efetue o login")
    login=input("Insira o e-mail cadastrado: ")
    chave=input("Insira a senha: ")
    if login==email and senha==chave:
        print("Login efetuado com sucesso!!")
    else:
        print("Algo esta errado!!")
else:
    print("Senha inválida")
