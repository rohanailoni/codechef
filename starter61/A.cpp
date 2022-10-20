
#include <bits/stdc++.h>
using namespace std;
long long aero[200001],bero[200001];
int main() {
    int t;cin>>t;
    while(t--){
        long long n;cin>>n;
        for(long long i = 1;i<=n;++i){
            cin>>aero[i];
        }
        if(n==1){
            cout<<"1"<<endl;
            continue;
        }
        for(long long i = 2;i<=n;++i){
            bero[i] = aero[i] < aero[i-1];
        }
        long long ans = 0;
        vector<pair<bool,long long>> kush;
        kush.push_back({bero[2],1});
        for(long long i = 3;i<=n;++i){
            if(bero[i] == kush[kush.size()-1].first){
                kush[kush.size()-1].second++;
            }
            else{
                kush.push_back({bero[i],1});
            }
        }
        kush.push_back({0,0});
        for(long long i = 0;i<kush.size()-1;++i){ans += kush[i].second*((kush[i].second+1)/2);}
        for(long long i = 0;i<kush.size()-1;++i){
            if(kush[i].first == 1){ ans += kush[i].second*kush[i+1].second;}
        }
        cout<<ans + n<<endl;
    }
    return 0;
}

