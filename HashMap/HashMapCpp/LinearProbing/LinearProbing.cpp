#include <iostream>
#define MAX 10
using namespace std;
int insert_linear_probe(int hashtable[],int key, int T[])
{
	int i,j;
	j=key%MAX;
	for(i=0;i<MAX;i++)
	{
		if(T[j]==0)
		{
			hashtable[j]=key;
			T[j] = 1;
			return(j);
		}
	j=(j+1)%MAX;/*next location in circularwat*/
	
	}
	///otherwise the table is ful;
	return(-1);
}


int search_linear_probe(int hashtable[], int key, int T[])
{
	int i,j;
	j=key%MAX;
	for(i=0;i<MAX;i++)
	{
		if(T[j]==1 && hashtable[j]==key)
			return(j);
		j=(j+1)%MAX;/*nnext location in circular way*/
		
	}
	//other not in table
	return(-1);
}

