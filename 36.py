from datetime import datetime

def verificar_data(data):
    try:
        # Tenta converter a string para um objeto de data no formato dd/mm/aaaa
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Solicita ao usuário para inserir a data
data_input = input("Digite uma data no formato dd/mm/aaaa: ")

if verificar_data(data_input):
    print(f"A data {data_input} é válida.")
else:
    print(f"A data {data_input} é inválida.")
