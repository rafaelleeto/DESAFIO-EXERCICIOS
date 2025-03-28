metros_quadrados=input("Digite quantos metros quadrados serão pintados")
metros_quadrados= int(metros_quadrados)


litros=metros_quadrados/6

preço_total=litros*4.4

latas_totais=preço_total/80

print(f"comprar apenas em latas de 18: {preço_total} ")
print(f"Comprar apenas em galões de 3,6 litros: {litros*0.14}")