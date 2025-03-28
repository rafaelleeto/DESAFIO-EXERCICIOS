while True:
    lado1=int(input("Digite o tamanho do lado do triangulo"))
    lado2=int(input("Digite o tamanho do lado do triangulo"))
    lado3=int(input("Digite o tamanho do lado do triangulo"))

    if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3< lado1+lado2:

        if lado1==lado2 and lado1==lado3:
            print("Equilatero")

        elif lado1==lado2 or lado1==lado3 or lado3==lado2:
            print("Isoceles")

        elif lado1!=lado2 and lado1!= lado3 and lado2!=lado3:
            print("escaleno")

    else:
        print("não pode formar um triangulo!")
        break