#include <iostream>
#define MAX 10
using namespace std;
struct node{
		int data;
		node *next;
};
	
node *hashtable[MAX];
	
void initialize(node *hashtable[])
{
	int i;
	for(i=0;i<MAX;i++)
		hashtable[i]=NULL;
}

void insert(node *hashtable[], int x)
{
	int loc;
	node *p, *q;
	loc = x%MAX;
	//get memory for new node
	q = new node;
	q -> data = x;
	q -> next = NULL;
	if(hashtable[loc] == NULL)
		hashtable[loc] = q;
	else
	{
		//lcoate the last node of the linked list
		for(p=hashtable[loc];p->next!=NULL;p=p->next);
		p->next = q;
	}
}

//Find
node *find(node *hashtable[], int x)
{
	int loc;
	node *p;
	loc= x%MAX;
	p=hashtable[loc];
	while(p!=NULL && x!=p->data)
		p=p->next;
	return(p);
}