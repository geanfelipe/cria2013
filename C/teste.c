#include <stdio.h>

int p(int,int);
int x;

int main()
{	
	int d, s, q;
	d = p(s, q);
	
	printf("x = %d e a funcao retornou %d \n", x, d);

	return 0;
}

int p(int s, int q){
	q=1;	
	s=q;
	x=10;
	return s;
}
