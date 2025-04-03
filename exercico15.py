produto_nome=input("Insira o nome do produto: ")
produto_quant=int(input("Insira quantas unidades do produto: "))
produto_valor_uni=float(input("Insira o valor da unidade do produto: "))
valor_total= produto_quant*produto_valor_uni
if valor_total>100:
    valor_total=valor_total*0.95
print(f"Total: R${valor_total}")