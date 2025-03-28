from cmath import sqrt


while True:

    a=int(input("Digite o valor de A"))

    if a==0:
        print("Não pode ser 0!")
        break

    b=int(input("Digite o valor de B"))

    c=int(input("Digite o valor de C"))

    delta=(b*b)-4*a*c

    if delta<0:
        print("Raiz reais não existem")
        break

    elif delta==0:
        print("O delta possui apenas uma raiz!")
    
    else:
        print(sqrt(delta))



