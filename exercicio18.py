#salario+horas extras
salario_base=float(input("Insira o salario base: "))
num_horas_extra=float(input("Insira o numéro de horas extras: "))
valor_hora_extra=float(input("Insira o valor a ser pago por hora extra: "))
salario_total=salario_base+(num_horas_extra*valor_hora_extra)
print(f"O salario total é R${salario_total}.")