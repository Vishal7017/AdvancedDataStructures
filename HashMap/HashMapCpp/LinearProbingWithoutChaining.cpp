/* Hashing */
/* Program Details - Hashing , hanndle collision usinnng linear probing without chaining */
#include <iostream>
using namespace std;
#define SIZE 10 /* size of the hash table */
#define FALSE 0
#define TRUE 1
#define h(x) x%SIZE /* hashing function */
void insert(int data[], int flag[], int x);
int search(int data[], int flag[], int x);
void print(int data[], int flag[]);

int main()
{
    int data[SIZE], flag[SIZE],i,j,x,op,loc;
    /* array data[] -is a hash table
    array flag[] - if flag[i] is 1 then the ith place of the hash table is filled */
    for(i=0;i<SIZE;i++) /*initialize*/
        flag[i]=FALSE;
    do
    {
        cout<<"\n\n1)Insert\n2)Search\n3)Print\n4)Quit";
        cout<<"\nEnter Your Choice:";
        cin>>op;
        switch(op)
        {
            case 1: cout<<"\nEnter a number to be inserted:";
                    cin >> x;
                    insert(data,flag,x);
                    break;
            
            case 2:cout<<"\nEnter a number to be searched:";
                   cin >> x;
                   if((loc=search(data,flag,x))==-1)
                   cout<<"\n***Element not found ***";
                   else
                   cout<<"\nFound at the location="<<loc;
                        break;
            
            case 3: print(data,flag);
                    break;
        }
    }while(op!=4);
}


void insert(int data[],int flag[], int x)
{
    int i,j;
    j=h(x);
    for(i=0;i<SIZE;i++)
    {
        if(flag[j]==FALSE)//empty location is found
        {
            data[j]=x;
            flag[j]=TRUE;
            return;
        }
        else
        j=(j+1)%SIZE;
    }
    cout<<"\n****hash table is full****";
}

int search(int data[], int flag[], int x)
{
    int i,j;
    j=h(x); /*hashed location*/
    for(i=0;i<SIZE;i++)
        if(flag[j]==TRUE && data[j]==x)
            return(j);
        else
            j=(j+1)%SIZE;
    return(-1);
}

void print(int data[],int flag[])
{
    int i;
    for(i=0;i<SIZE;i++)
        if(flag[i])
            cout<<"\n("<<i<<") " <<data[i];
        else
            cout<<"\n("<<i<<") ---";
}
