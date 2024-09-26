#include <stdio.h>

int main(){
    float f,g;
    printf("Digite quantos graus farenheint: ");
    scanf("%f",&f);
    g = (5 * (f-32) / 9);
    printf("Em graus celsius sao: %.2f",g);

    return 0;
}