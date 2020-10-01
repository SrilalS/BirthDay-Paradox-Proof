#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int find(double p)
{
    return ceil(sqrt(2*365*log(1/(1-p))));
}
int main()
{
    double p;
    cout<< "Enter the probabilty between 0 and 1(exclusive)";
    cin>>p;
    cout<<find(p);
    return 0;
}