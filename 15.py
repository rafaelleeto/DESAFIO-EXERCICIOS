dinheiro_hora=float(input("Digite quanto você ganha por hora! "))
horas_trabalhadas=int(input("Digite quantas horas foram trabalhadas! "))


salario_total=dinheiro_hora*horas_trabalhadas
descontos=salario_total*0.11+salario_total*.008+salario_total*0.05
print("Salario bruto: ",salario_total)
print("IR: ",salario_total*0.11)
print("INSS: ",salario_total*0.08)
print("Sindicato: ",salario_total*0.05)
print("Salario líquido: ",salario_total-descontos)

