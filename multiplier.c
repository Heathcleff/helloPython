/*
 * multiplier.c
 * author @zeshen
 * function -  Multiplier operation
*/

#include <stdio.h>
#include <stdlib.h>

int main(void){
	int x,y,i,a;
	printf("请输入底数:\n");
	scanf_s("%d",&x);
	a=x;
	printf("\n请输入指数:\n");
	scanf_s("%d",&y);
	
	for(i=1;i<y;i++){
		x=a*x;
	}
	printf("计算结果为：%d",x);
	return x;
}

