#include <stdio.h>

int main() {
    int i = 0, q = 0, w = 0, e = 0, r = 0, s = 0, t = 0;
    char a;
    while(1){
        scanf("%c", &a);
        if(a == ' '){
            break;
        }
        else if(a == '('){
            q++;
        }
        else if(a == ')'){
            w++;
        }
        else if(a == '['){
            e++;
        }
        else if(a == ']'){
            r++;
        }
        else if(a == '{'){
            s++;
        }
        else if(a == '}'){
            t++;
        } 
    }
    if(q == w && e == r && s == t){
        printf("True");
    }
    else{
        printf("False");
    }
}
