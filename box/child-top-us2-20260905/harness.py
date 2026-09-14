import sys; sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
import sympy as sp
from fractions import Fraction
from chardata import chardata

def effective(cd):
    """Apply the p.174 Definition-Remark: drop M_h if M_h = n-1.  Return (s, Ms, ds)."""
    n = cd['n']; M = [v for v in cd['M'] if v is not None and v != 'TRUNCATION-RISK']
    dropped = False
    if M and M[-1] == n-1:
        M = M[:-1]; dropped = True
    return len(M), M, cd['d'], dropped

def analyse(f, g, x, y, label=''):
    cy = chardata(f, g, y, x)          # y-side  (Moh's own: param=y, base=x)
    cx = chardata(f, g, x, y)          # x-side
    n = cy['n']; nt = cx['n']
    s, Ms, ds, dropped = effective(cy)
    if s == 0: return None
    d_s = ds[s-1]                      # ds = [d_1,d_2,...]; d_s is ds[s-1]
    us_num = Fraction(nt*d_s, n)
    out = dict(label=label, n=n, m=cy['m'], nt=nt, mt=cx['m'],
               M=cy['M'], d=cy['d'], Mx=cx['M'], dx=cx['d'],
               s=s, d_s=d_s, dropped_parent=dropped, u_s=str(us_num),
               Ms_is_n_minus_2=(Ms[-1] == n-2))
    if us_num.denominator != 1: out['u_s_integral'] = False; return out
    us = int(us_num); out['u_s'] = us
    out['u_s_integral'] = True
    # banked closed form  M'_i = M_i * u_s/d_s  for i <= s-1, checked against the x-side
    pred = [Fraction(Mi*us, d_s) for Mi in Ms[:s-1]]
    Mx = [v for v in cx['M'] if v is not None and v != 'TRUNCATION-RISK']
    out['pred_low'] = [str(p) for p in pred]
    out['obs_low'] = Mx[:s-1]
    out['low_match'] = (len(Mx) >= s-1 and all(p.denominator==1 and int(p)==o
                                               for p,o in zip(pred, Mx[:s-1])))
    out['dx_s_eq_us'] = (len(cx['d']) >= s and cx['d'][s-1] == us)
    out['M_extra'] = Mx[s-1:]
    out['nt_minus_1'] = nt-1
    out['CTOP_hypothesis'] = (len(Mx) >= s and Mx[s-1] == nt-1 and len(Mx) == s)
    return out
