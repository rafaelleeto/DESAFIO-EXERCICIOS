letras=[]
auxiliar=int
letra1=[]
letra2=[]
letra3=[]

def executar(centena,dezena,unidade):
    if centena!="0" and dezena!="0" and unidade!="0": # Faz a verificação para que não tenha NENHUM zero

        if centena=="1" and dezena=="1" and unidade=="1":
            print(f"1 centena ,1 dezena e 1 unidade")
        
        if centena=="1" and dezena=="1" and unidade!="1":
            print(f"1 centena ,1 dezena e {unidade} unidades")
        
        if centena=="1" and dezena!="1" and unidade!="1":
            print(f"1 centena ,{dezena} dezenas e {unidade} unidades")
        
        if centena!="1" and dezena!="1" and unidade!="1":
            print(f" {centena} centenas ,{dezena} dezenas e {unidade} unidades")
            
        
        if unidade=="1" and dezena=="1" and centena!="1":
            print(f"{centena} centenas, 1 dezena e 1 unidade")

        if unidade=="1" and dezena!="1" and centena!="1":
            print(f"{centena} centenas, {dezena} dezenas e 1 unidade")
           
        
        if unidade!="1" and dezena=="1" and centena!="1":
            print(f"{centena} centenas, 1 dezena e {unidade} unidades")



    
    if centena=="0" or dezena=="0" or unidade=="0": # faz a verificação CASO houver zeros
        if centena=="0" and dezena=="0" and unidade=="0":
            print("0 centena, 0 dezena e 0 unidade")
        
        if centena=="0" and dezena=="0" and unidade!="0":
            if unidade=="1":
                print("0 centena, 0 dezena 1 unidade")
            
            else:
                print(f"0 centena, 0 dezena e {unidade} unidades")

        
        if centena=="0" and dezena!="0" and unidade!="0":
            if dezena=="1" and unidade=="1":
                print("0 centena, 1 dezena 1 unidade")
            if dezena!="1" and unidade=="1":
                print(f"0 centena, {dezena} dezenas e 1 unidade")
               

            if dezena!="1" and unidade!="1":
                print(f"0 centena, {dezena} dezenas e {unidade} unidades")
              
        
        if centena=="0" and dezena!="0" and unidade=="0":
            if dezena=="1":
                print(f"0 centena, 1 dezena e 0 unidade")
               
            else:
                print(f"0 centena, {dezena} dezenas e 0 unidade")
        
        if centena!="0" and dezena=="0" and unidade=="0":
            if centena=="1":
                print("1 centena, 0 dezena e 0 unidade")
            else:
    
                print(f"{centena} centenas ,0 dezena e 0 unidade")

        if centena!="0" and dezena!="0" and unidade=="0":
            if centena=="1" and dezena=="1":
                print("1 centena, 1 unidade, e 0 dezena")
            if dezena=="1" and centena!=1:
                print(f"{centena} centenas, 1 dezena e 0 unidade")
        
        if centena!="0" and dezena=="0" and unidade!="0":
            if centena=="1" and unidade=="1":
                print("1 centena, 0 dezena e 1 unidade")
            if centena!="1" and unidade=="1":
                print(f"{centena} centenas, 0 dezena e 1 unidade")
            
            if centena>"1" and unidade>"1":
                print(f"{centena} centenas, 0 dezena e {unidade} unidades")
                
    
        if centena>"1" and dezena>"1" and unidade=="0":
            print(f"{centena} centenas, {dezena} dezenas e 0 unidade")

        if centena=="0" and dezena=="1" and unidade>"1":
            print (f"0 centena, 1 dezena e {unidade} unidades")
    
    
while True:   
    print("\nDigite um numero! ")
    verificacao=int(input(""))
    if verificacao>999 or verificacao<0:
        print("\nParece que você digitou um valor acima de 999 e abaixo de 0!, tente novamente!")
        verificacao=int(input(""))
        
    letras=str(verificacao)


    for i in  range(len(letras)):
            
        if len(letras) > 2 and letras[i] >= letras[2]:
            auxiliar=3
        elif len(letras) > 1 and letras[i]>=letras[1]:
            auxiliar=2
            
        else:
            auxiliar=1

    if auxiliar==3:
        for i in range(len(letras)):
                letra1=letras[0]
                letra2=letras[1]
                letra3=letras[2]
                executar(letra1,letra2,letra3)
                break

    elif auxiliar==2:
        for i in range(len(letras)):
            letra1=letras[0]
            letra2=letras[1]
            executar("0",letra1,letra2)
            break
            

    else :
        for i in range(len(letras)):
            letra3=letras[0]
            executar("0","0",letra3)
            break
