#include<stdio.h>
void fun(int x){
	static int cnt=1;
	int i;
	for(i=2;i<=x;i++){
		if(x%i==0){
			if(cnt==1){
				printf("%d",i);
				cnt++;
			}
			else{
				printf("*%d",i);
			}
			fun(x/i);
			break;
		}
	}
	if(x==1) return;
}
int main(){
	int num;
	scanf("%d",&num);
	fun(num);
	return 0;
}
