#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
    
    long max_value = pow(10, 8);
    long *primes = malloc(sizeof(long) * (max_value));

    primes[0] = 2;
    int num_primes = 1;

    for(long long i = 3; i < max_value; i+=2){
        for(int j = 0; j < num_primes; j++){
            if(primes[j] * primes[j] > i){
                primes[num_primes++] = i;
                break;
            }
            if(i % primes[j] == 0){
                break;
            }
        }
    }

    printf("%d", num_primes);
}