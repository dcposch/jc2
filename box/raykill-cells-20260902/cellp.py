import sympy as sp
from cell import build_cell
Z=sp.symbols('Z')
def build_primed(e,U):
    """cell system PLUS the proved pins: wall (HORN-A2), ray (HORN-A2), and RAY-1/RAY-2 (top-1)."""
    eqs,V,info=build_cell(e,U)
    g,m,n,sig=info['g'],info['m'],info['n'],info['sig']
    S=lambda i: sp.Symbol('S%d'%i); Qs=lambda i: sp.Symbol('Q%d'%i)
    Rs=lambda i: sp.Symbol('R%d'%i); Gs=lambda i: sp.Symbol('G%d'%i); As=lambda i: sp.Symbol('A%d'%i)
    Ae=sp.Integer(1)                      # A_e normalised to 1 by the mu-scaling
    Ss,Qm,Rn=S(sig),Qs(m),Rs(n)
    pins=[ 4*Rn - Ss**2,                                   # R_n = S^2/(4 b A^2),  a=b=A=1
           4*Qm - 3*Ss**2,                                 # Q_m = 3a S^2/(4 b^2 A)
           Gs(g-1) + 4*e*As(e-1) if e>=1 else Gs(g-1),     # ehat = 0  (RAY-2)
           2*Ss*Rn*As(e-1) - (2*S(sig-1)*Rn - Ss*Rs(n-1)),     # alpha = beta - delta/2
           2*Ss*Rn*Qs(m-1) - Qm*(2*S(sig-1)*Rn + Ss*Rs(n-1))]  # gamma = beta + delta/2
    return [sp.expand(p) for p in pins]+eqs, V, info
