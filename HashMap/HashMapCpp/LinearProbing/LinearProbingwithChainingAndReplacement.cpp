/*Hashing*/
/* Porgram Details - Hashing , handle collision using linear probing with chaining and with replacement */

#include<iostream>
using namespace std;

#define SIZE 10   /* size of the hash table */
#define FALSE 0
#define TRUE 1
#define h(x) x%SIZE /*hashing function*/

void insert(int data[], int flag[], int chain[],int x);
int search(int data[], int flag[], int chain[], int x);
void print(int data[], int flag[], int chain[], int x);

int main()
{
    int data[SIZE],flag[SIZE],chain[SIZE],i,j,x,op,loc;
    /* array data[] - is a hashtable
       array flag[] - if flag[i] is 1 then thhe ith place of the hash table is filled */
    for(i=0;i<SIZE;i++)/* initialize */
    {
        flag[i]=FALSE;
        chain[i]=-1;
    }
    do
    {
        cout<<"\n\n1)Insert\n2)Search\n3)Print\n4)Quit";
        cout<<"\nEnter Your Choice : ";
        cin>>op;
        switch(op)
        {
            case 1: cout<<"\n Enter a number to be inserted:";
                    cin>>x;
                    insert(data,flag,chain,x);
                    break;
            
            case 2: cout<<"\nEnter a number to be searched :";
                    cin>>x;
                    if((loc=search(data,flag,chain,x))==-1)
                        cout<<"\n****Element not found****";
                    else
                        cout<<"\n****Found at the location= "<<loc;
                    break;
            
            case 3: print(data,flag,chain);
                    break;
        }
    }while(op!=4);
}

void insert( int data[],int flag[], int chain[], int x)
{
    int i=0,j,start;
    start=h(x); /*hashed location */
    /*Situation I,hashed location is empty*/
    if(flag[start]==0)
    {
        data[start]=x;
        flag[start]=1;
        return;
    }

    /*Situation II, hashed location does not contain a synonym*/
    if(h(data[start])!=h(x))
    {
        /*locate an empty location */
        i=0;j=start;
        while(flag[j] && i<SIZE)
        {
            j=(j+1)%SIZE;
            i++;
        }
        if(i==SIZE)
        {
            cout<<"\nTable is Full...";
            return;
        }
        /* Delete the element by modifying the chain */
        i=data[start]&SIZE; /*beginning of the chain */
        while(chain[i]!=start)
            i=chain[i];
            chain[i]=chain[start]; /*modify*/
            /* add the deleted element at the endof the chain */
            while(chain[i]!=-1)
                i=chain[i];
                chain[i]=j;
                data[j]=data[start];
                chain[start]=-1;
                flag[i]=1;
                chain[j]=-1;
                /*insert the current key */
                data[start]=x;
                chain[start]=-1;
                return;
    }
    /* Situation III, hashed location conatins a synonym */
    /* locate an empty location */
    i=0;j=start;
    while(flag[j] && i<SIZE)
    {
        j=(j+1)%SIZE;
        i++;
    }
    if(i==SIZE)
    {
        cout<<"\nTable is full....";
        return;
    }

        data[j]=x;
        flag[j]=1;
        chain[j]=-1;
        /* go to the end of chain */
        i=start;/*beginning of the chain */
        while(chain[i]!=-1)
            i=chain[i];
        chain[i]=j;
}

int search(int data[], int flag[], int chain[], int x)
{
    
}