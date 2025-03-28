#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes 
# fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7


while True:
    genero = input(("Digite se você é homem ou mulher com h/m"))

    if genero=="f":
        peso = float(input("Digite seu peso "))
        print("Seu peso ideal é de :",(62.1*peso) - 44.7)

    elif genero=="m":
        peso = float(input("Digite seu peso "))
        print("Seu peso ideal é de :",(72.7*peso) - 58 )


    else:
        print("Algo deu errado, tente novamente")


