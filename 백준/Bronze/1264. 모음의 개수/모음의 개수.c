#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str[255];
    
    int len,i,cnt=0;
    int ans[100], j = 0;
    
    while (1) {
        cnt = 0;
        gets(str);
        if (str[0] == '#') break;
        len = strlen(str);

        for (i = 0; i < len; i++) {
            if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u'
                || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i]=='U') {
                cnt++;
            }
        }
        ans[j] = cnt;
        j++;
        
    }
    
    for (i = 0; i < j; i++) {
        printf("%d\n", ans[i]);
    }

    return 0;
}