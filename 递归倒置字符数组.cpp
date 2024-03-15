#include<stdio.h>
#include<string.h>
int start=0,end=0; 
void printA(char a[]){
	for(int i=0;i<strlen(a);i++)
		printf("%c",a[i]);
}
void swap(char *a,char *b){
	char t;
	t=*a;*a=*b;*b=t;
}
void fun(char a[],int start,int end){
	if(start>=end) return;
	else{
		swap(&a[start],&a[end]);
		printA(a);
		printf("\n");
		start++;end--;
		fun(a,start,end);
	}
}
int main(){
	int n;
	scanf("%d",&n);
	char a[n];
	getchar();
	for(int i=0;i<n;i++)
		scanf("%c",&a[i]);
	end=n-1;
	fun(a,start,end);
	if(n==1) printf("\n%c",a[0]);
	else{
		printf("\n");
		printA(a);
	} 
}
