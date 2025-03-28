
nota1=int(input("Digite sua nota"))
nota2=int(input("Digite sua nota"))
media=(nota1+nota2)/2
print(media)

if media >=9.0:
    print(media)
    print("A")
    print("Aprovado")

elif media<9.0 and media>7.5:
    print(media)
    print("B")
    print("Aprovado")

elif media<7.5 and media>6:
    print(media)
    print("C")
    print("Aprovado")

elif media<6 and media>4:    
    print(media)
    print("D")
    print("Reprovado")

elif media<4 and media>0:
    print(media)
    print("E")
    print("Reprovado")