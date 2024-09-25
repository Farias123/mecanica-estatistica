#include <stdio.h>
#include <math.h>

void main(){
    double r[2] = {1.0, 1.0};
    double v[2] = {0.5, 0.0};
    
    double t = 0.0;
    double dt = 0.1;
    
    double f[2], f_[2];
    
    double phi(double q){
        return -q;
    }

    int i;
    while(t<10){
        f[0] = phi(r[0]);
        f[1] = phi(r[1]);
        
        for(i = 0; i<2; i+=1){
            r[i] += dt*v[i] + 1/2*f[i]*pow(dt, 2);
        }
        
        f_[0] = phi(r[0]);
        f_[1] = phi(r[1]);
        
        for(i = 0; i<2; i+=1){
            v[i] += dt*(f[i]+f_[i])/2;
        }
        printf("%f, %f\n", r[0], r[1]);
    }
}