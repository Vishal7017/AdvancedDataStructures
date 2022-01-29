/*Hashing*/
/* Porgram Details - Hashing , handle collision using linear probing with chaining and with replacement */

#include<iostream>
using namespace std;

#define SIZE 10   /* size of the hash table */
#define FALSE 0
#define TRUE 1
#define h(x) x%SIZE /*hashing function*/
