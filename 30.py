ir=float
inss=float
salario_liquido=float

dinheiro_hora=float(input("Digite quanto de dinheiro voce ganhar por hora"))
horas_trabalhadas=float(input("Digite quantas horas você trabalhou!"))

print(f"Salario bruto: {dinheiro_hora*horas_trabalhadas}")
print(f"IR: {0.05*(dinheiro_hora*horas_trabalhadas)}")
print(f"INSS: {0.10*(dinheiro_hora*horas_trabalhadas)}")
print(f"FGTS: {0.11*(dinheiro_hora*horas_trabalhadas)}")
print(f"Total de descontos: {0.05*(dinheiro_hora*horas_trabalhadas)+0.10*(dinheiro_hora*horas_trabalhadas)}")
print(f"Salario liquido: {dinheiro_hora*horas_trabalhadas-(0.05*(dinheiro_hora*horas_trabalhadas)+0.10*(dinheiro_hora*horas_trabalhadas))} ")