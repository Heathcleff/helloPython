/*
 * multiplier.c
 * author @zeshen
 * function -  Multiplier operation
*/

#include <stdio.h>
#include <stdlib.h>

int main(void){
	int x,y,i,a;
	printf("���������:\n");
	scanf_s("%d",&x);
	a=x;
	printf("\n������ָ��:\n");
	scanf_s("%d",&y);
	
	for(i=1;i<y;i++){
		x=a*x;
	}
	printf("������Ϊ��%d",x);
	return x;
}
