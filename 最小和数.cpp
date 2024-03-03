#include<stdio.h>
#include<math.h>
int gcd(int x,int y){
	if(x%y==0)
		return y;
	else
		return gcd(y,x%y);
}
int main(){
	int L,G;
	scanf("%d%d",&G,&L);
	int minsum,sum,num1,num2;
	num1=L/G;
	num2=sqrt(num1);
	minsum=num1+1;
	for(int i=1;i<=num2;i++){
		for(int j=num2;j<=num1;j++){
			if(i*j==num1&&gcd(i,j)==1){
				sum=i+j;
				if(sum<minsum) 
					minsum=sum;
				break;
			}
		}
	}
	if(L==1) minsum=L+G;
	printf("%d",minsum*G);
	return 0;
}
