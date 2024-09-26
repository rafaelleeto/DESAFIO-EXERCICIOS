#include <stdio.h>

void bimestre(){

float nota1,nota2,nota3,nota4,media,total;
    printf("Informe as 4 notas: ");
    scanf("%f %f %f %f",&nota1,&nota2,&nota3,&nota4);
    total=nota1+nota2+nota3+nota4;
    media=total/4;
    printf("a média total é: %.2f",media);

}
int main(){
    
    bimestre();
    return 0;


}