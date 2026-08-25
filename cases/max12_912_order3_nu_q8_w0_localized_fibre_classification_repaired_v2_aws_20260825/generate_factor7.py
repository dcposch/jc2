#!/usr/bin/env python3
"""Emit an independent Singular factor-count certificate for Q8 mod 7."""

print(r'''ring R=7,(v),dp;
option(redSB);
poly q=v^8+4*v^7+2*v^6+v^5+6*v^4+2*v^3+4*v^2+v+5;
list L=factorize(q,1);
ideal F=L[1];
intvec M=L[2];
int count=size(F);
int degree_sum=0;
int degree8_count=0;
int multiplicity_one=1;
int product_ok=0;
poly prod=1;
for(int i=1;i<=count;i++){
  int di=deg(F[i]);
  degree_sum=degree_sum+di*M[i];
  if(di==8){degree8_count=degree8_count+1;}
  if(M[i]!=1){multiplicity_one=0;}
  for(int j=1;j<=M[i];j++){prod=prod*F[i];}
  print("factor_"+string(i)+"_degree="+string(di));
  print("factor_"+string(i)+"_multiplicity="+string(M[i]));
  print("factor_"+string(i)+"="+string(F[i]));
}
if(reduce(q,std(ideal(prod)))==0 && reduce(prod,std(ideal(q)))==0){product_ok=1;}
print("factor_count="+string(count));
print("degree_sum="+string(degree_sum));
print("degree8_count="+string(degree8_count));
print("multiplicity_one="+string(multiplicity_one));
print("mutual_divisibility="+string(product_ok));
if(count==1 && degree_sum==8 && degree8_count==1 && multiplicity_one==1 && product_ok==1){
  print("Q8_MOD7_SINGULAR_IRREDUCIBLE_PASS");
}
exit;''')
