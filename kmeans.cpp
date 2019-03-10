#include<iostream>
#include<cmath>
using namespace std;
int main(){

int x[6]={0,2,40,10,80,100};
int x1[6],x2[6],y1[6],y2[6];
int y[6]={10,0,1,60,10,56};
int i1,j1,i2,j2,k=2,i,j=0,c=0,r=0;
int a,b;
i1=x[1];
j1=y[1];
i2=x[3];
j2=y[3];
cout<<endl;
while(r=1){
        int s2=0,s1=0,t1=0,t2=0;
        j=0;
        c=0;
for(i=0;i<6;i++)
{
    //cout<<array1[i]<<" ";
    a=sqrt(((x[i]-i1)*(x[i]-i1))+((y[i]-j1)*(y[i]-j1)));
    b=sqrt(((x[i]-i2)*(x[i]-i2))+((y[i]-j2)*(y[i]-j2)));
    cout<<a<<" "<<b<<endl;
    if(a<b){
        x1[c]=x[i];
        s1=s1+x[i];
        y1[c]=y[i];
        s2=s2+y[i];
        c++;}
    else
    {
        x2[j]=x[i];
        t1=t1+x[i];
        y2[j]=y[i];
        t2=t2+y[i];
        j++;
    }
}

s1=s1/c;
s2=s2/c;
t1=t1/j;
t2=t2/j;
if(i1==s1 && j1==s2 && i2==t1 && j2==t2){
     r=1;
     break;
}

else{
    i1=s1;
    j1=s2;
    i2=t1;
    j2=t2;
    }

}


cout<<"x1"<<" "<<"y1"<<endl;
for(i=0;i<c;i++)
{

    cout<<x1[i]<<" "<<y1[i]<<endl;
}
cout<<endl<<"x2"<<" "<<"y2"<<endl;
for(i=0;i<j;i++)
{
    cout<<x2[i]<<" "<<y2[i]<<endl;
}



return 0;
}
