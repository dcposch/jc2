#!/usr/bin/env python3
"""Exact rational identities used in the uniform direct coefficient proof."""
import sympy as s

d,y,k=s.symbols('d y k')
t=3*d*d-1;q=2*t+1
alpha=3/(4*y*y);delta=3/(2*y)
omega=3*(2*d-1)/(4*y*y*(4*t+1))
nu=delta*(omega-alpha/3)/(2*((q+t-1)*omega+alpha))
checks={
    'OMEGA':omega-1/(4*y*y*(2*d+1)),
    'HIGH_W_PIVOT':2*((q+k-1)*omega+alpha)
      -(6*d*(d+1)+k+1)/(2*y*y*(2*d+1)),
    'B_PIVOT':-((2*q-1)*omega+alpha)+3*d/(2*y*y),
    'MONOMIAL_C_Q_LEAD':nu+1/(2*y*(3*d+2)),
}
E=(2*t-1)*nu*nu-delta*nu-((2*t-1)*omega+alpha)/2
checks['B2_AXIS']=E-3*(d+1)*(1-8*d*d-9*d**3)/(4*y*y*(3*d+2)**2*(2*d+1))
checks['B3_AXIS']=-(t-2)*nu/2-(t-2)/(4*y*(3*d+2))
actualE=E.subs(y,(d+t+1)/(2*q))
normE=-9*q**4*(t-2)*(27*t**3+17*t*t+t+2)/((t+1)**2*(3*t+2)**2*(3*t-1)**2*(4*t+1))
checks['B2_AXIS_NORM']=actualE*actualE.subs(d,-d)-normE
for name,expr in checks.items():
    assert s.cancel(expr)==0,name
    print(name+'_PASS')
print('UNIFORM_IDENTITIES_DONE')
