#include<iostream>
using namespace std;
int main()
{
	int Rows, i, j;
	printf(" Please Enter the Number of Rows: ");
	scanf("%d", &Rows);
	
	printf(" \n Printing FLOYD'S Triangle \n \n");
	for(i= 1;i<=Rows;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("* ");
		}
		printf("\n");
	}
	return 0;
}