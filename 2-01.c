#include <stdio.h>

int main(){
	int n, m, c, max = 0, min = 10, i, j;
	int mi[100];
	printf("행 개수, 열 개수 입력\n");
	scanf("%d %d", &n, &m);
	int a[n][m];
	printf("배열 입력\n");
	for(i = 0; i < n; i++){
		for(j = 0; j < m; j++){
			scanf("%d", &a[i][j]);
			if(min >= a[i][j]){
				mi[i] = a[i][j];
				min = a[i][j];
			}
		}
		min = 10;
	}
	for(i = 0; i < n; i++){
		if(max <= mi[i]){
			max = mi[i];
		}
	}
	printf("출력 : %d", max);
}
