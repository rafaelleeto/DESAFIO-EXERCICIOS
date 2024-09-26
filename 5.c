#include <stdio.h>

int main(){
    float metros,centimetros;
    printf("Digite quantos metros voce deseja converter para centimetros: ");
    scanf("%f",&metros);
    centimetros=metros*100;
    printf("Convertido para centimentros e : %.2f",centimetros);
    
    return 0;
}


