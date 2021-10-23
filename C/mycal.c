#include <stdio.h>

int main(){
    printf("   Sun    Mon    Tue    Wed    Thu    Fri    Sat\n");
    printf("                    ");
    for (int i = 1; i <=14 ; i++){
        if(i%7==0){
            printf("       ");
        }
    }
    for (int i = 1; i <= 31; i++){
        printf("%7d",i);
        if((i+5)%7==0){
            printf("\n");
        }
        
    }

}