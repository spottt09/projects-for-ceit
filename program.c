#include <stdio.h>
int main(){
    
    for(int a=5;a>=1;a--){
        for(int b=1;b<=a;b++){
            printf("%d  ",a);
        }printf("\n");
    }
    return 0;
}