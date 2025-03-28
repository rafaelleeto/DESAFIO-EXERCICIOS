
salario=float(input("Digite o seu salário!"))
salario_reajuste=float
porcentagem=str
aumento=float

if salario < 280:
    salario_reajuste=salario+(salario*0.20)
    porcentagem = "20%"
    aumento=salario*0.20

elif salario>=280 and salario <=700:
    salario_reajuste=salario+(salario*0.15)
    porcentagem = "15%"
    aumento=salario*0.15

elif salario >700 and salario <1500:
    salario_reajuste=salario+(salario*0.10)
    porcentagem = "10%"
    aumento=salario*0.10
else: 
    salario_reajuste=salario+(salario*0.05)
    porcentagem = "5%"
    aumento=salario*0.05

print(f"salario antes do reajuste: {salario} ")
print(f"porcentagem : {porcentagem} ")
print(f"valor do aumento: {aumento} ")
print(f"Novo Salario : {salario_reajuste} ")