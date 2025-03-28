numeros = []

# Coleta os números
for i in range(3):
    number = int(input("Digite um numero: "))  # Converte para inteiro
    numeros.append(number)
    print(f"Número digitado: {numeros[i]}")

# Ordena os números em ordem decrescente
numeros_decrescente = sorted(numeros, reverse=True)

# Exibe os números em ordem decrescente
print("Números em ordem decrescente:", numeros_decrescente)