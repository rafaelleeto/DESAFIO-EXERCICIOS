#include <stdio.h>

int main(){
    int horas;
    float dinheiro,total;
    printf("Digite quantas horas você trabalhou no mês: ");
    scanf("%d",&horas);
    printf("Digite quanto você recebe por hora: ");
    scanf("%f",&dinheiro);
    total=horas*dinheiro;
    printf("Você ganha no mês um total de : %.2f",total);


    return 0;
}