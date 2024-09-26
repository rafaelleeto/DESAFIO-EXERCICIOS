#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main (){
    float raio,raio2,area;
    printf("Digite o raio do circulo: ");
    scanf("%f",&raio);
    raio2=raio*raio;
    area=raio2*M_PI;
    printf("A area total é de: %.100f",area);
    return 0;
}